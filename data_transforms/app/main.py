import logging
from typing import Dict
from motor.motor_asyncio import AsyncIOMotorClient
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


async def transform_save_track_lyric(db: Database, track: Dict):
    doc = flow(
            track,
            lambda track: track.get('lyric')[0].get('fullLyrics'),
            transforms.lyric_pipeline,
            lambda doc: doc.as_json,
            lambda doc: {
                '_id': track.get('_id'), 
                'tokens': doc.tokens
            }
        )

    await db.insert_track_with_tokens(doc)


async def transform_save_tracks_lyrics(db: Database):
    cursor = db.tracks_with_lyric()

    async for track in tqdm(cursor):
        await flow(
            track,
            lambda track: track.get('lyric')[0].get('fullLyrics'),
            transforms.lyric_pipeline(track.get('_id')),
            db.insert_track_with_tokens
        )


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

    await transform_save_tracks_lyrics(db)


if __name__ == '__main__':
    asyncio.run(main())
