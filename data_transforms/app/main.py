import logging
from typing import Dict
from motor.motor_asyncio import AsyncIOMotorClient
from returns.curry import curry
from db import Database
from returns.pipeline import flow
from tqdm.asyncio import tqdm
import transforms
import asyncio
import config


logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')


async def artists_graph(db: Database, graph_name: str):
    cursor = db.artists_with_genres()
    artists = await cursor.to_list(length=None)
    
    graph = transforms.create_artists_graph(graph_name, artists)
    graph.save(f'{graph_name}_{len(artists)}.gv')


@curry
async def insert_track_with_tokens(db: Database, track: Dict):
    return db.insert_track_with_tokens(track)


async def track_lyric_flow(db: Database, track: Dict):
    await flow(
        track,
        lambda track: track.get('lyric')[0].get('fullLyrics'),
        transforms.lyric_pipeline(track.get('_id')),
        insert_track_with_tokens(db)
    )


async def tracks_lyrics(db: Database):
    cursor = db.tracks_with_lyric()

    async for track in tqdm(cursor):
        await track_lyric_flow(db, track)


async def main():
    client = AsyncIOMotorClient(config.MONGO_URL)
    db = Database(
        client, 
        config.DATABASE_NAME, 
        config.ARTISTS_COLLECTION_NAME,
        config.ARTISTS_INFO_COLLECTION_NAME, 
        config.TRACKS_COLLECTION_NAME,
        config.TRACKS_TOKENS_COLLECTION_NAME
    )
    
    await artists_graph(db, 'artists_graph')


if __name__ == '__main__':
    asyncio.run(main())
