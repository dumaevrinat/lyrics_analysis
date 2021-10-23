import time
import logging
import asyncio
import config
from asyncio.locks import Semaphore
from argparse import ArgumentParser
from typing_extensions import Literal
from tqdm.asyncio import tqdm
from motor.motor_asyncio import AsyncIOMotorClient
from data_parser import Parser
from session import get_cookies
from db import Database
from session import create_session, agents


logging.basicConfig(level=logging.WARNING, format='%(asctime)s : %(levelname)s : %(message)s')


async def parse_save_tracks(
    semaphore: Semaphore,
    parser: Parser, 
    db: Database,
    artist_id: str
):
    async with semaphore:
        track_infos = await parser.parse_tracks_from_artist(artist_id)
        
        if track_infos:
            await db.insert_tracks(track_infos)


async def parse_save_artist_info(
    semaphore: Semaphore,
    parser: Parser,
    db: Database,
    artist_id: str
):
    async with semaphore:
        artist_info = await parser.parse_artist_info(artist_id)

        if artist_info:
            await db.insert_artist_info(artist_info)


async def main(
    metatag: str, 
    concurrent_tasks: int, 
    what: Literal['tracks', 'infos'],
    session_timeout: int = 60*60
):
    client = AsyncIOMotorClient(config.MONGO_URL)
    db = Database(
        client, 
        config.DATABASE_NAME, 
        config.ARTISTS_COLLECTION_NAME,
        config.ARTISTS_INFO_COLLECTION_NAME, 
        config.TRACKS_COLLECTION_NAME
    )

    semaphore = Semaphore(concurrent_tasks)
    
    start = time.time()

    async with create_session(agents, get_cookies(config.COOKIES_FILE_PATH), session_timeout) as session:
        parser = Parser(session)
        
        artist_infos = await parser.parse_all_artists_from_metatag(metatag)
        artist_ids = [artist_info.get('artist').get('id') for artist_info in artist_infos]

        if what == 'tracks':
            await db.insert_artists(artist_infos)

            await tqdm.gather(
                *[parse_save_tracks(semaphore, parser, db, artist_id) for artist_id in artist_ids]
            )
        elif what == 'infos':
            await tqdm.gather(
                *[parse_save_artist_info(semaphore, parser, db, artist_id) for artist_id in artist_ids]
            )

    end = time.time()

    total_time = end - start
    print(f'Total time: {total_time}')


if __name__ == '__main__':
    parser = ArgumentParser(description='Parse artists and tracks from metatag')
    
    parser.add_argument('metatag', type=str, help='metatag for parsing artists and tracks')
    parser.add_argument('what', type=str, choices=['tracks', 'infos'], help='data type to parse')
    parser.add_argument('concurrent_tasks', type=int, help='number of concurrent tasks')

    args = parser.parse_args()

    asyncio.run(main(args.metatag, args.concurrent_tasks, args.what))
