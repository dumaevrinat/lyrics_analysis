import logging
from motor.motor_asyncio import AsyncIOMotorClient
from db import Database
import transforms
import asyncio
import config


logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')


async def artists_graph(db: Database, graph_name: str):
    cursor = db.artists_with_genres()
    artists = await cursor.to_list(length=None)
    
    graph = transforms.create_artists_graph(graph_name, artists)
    graph.save(f'{graph_name}_{len(artists)}.gv')


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
