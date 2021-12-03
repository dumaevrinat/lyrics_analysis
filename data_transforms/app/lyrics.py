import logging
from typing import Dict
from motor.motor_asyncio import AsyncIOMotorClient
from returns.curry import curry
from db import Database
from returns.pipeline import flow
from aio_pika import connect
import transforms
import asyncio
import config
import json


logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

loop = asyncio.get_event_loop()


@curry
async def insert_track_with_tokens(db: Database, track: Dict):
    await db.insert_track_with_tokens(track)


async def track_lyric_flow(db: Database, track: Dict):
    await flow(
        track,
        lambda track: track.get('lyric')[0].get('fullLyrics'),
        transforms.lyric_pipeline(track.get('_id')),
        insert_track_with_tokens(db)
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
    
    connection = await connect(config.QUEUE_URL)

    channel = await connection.channel()

    await channel.set_qos(prefetch_count=100)

    queue = await channel.declare_queue(
        config.QUEUE_ROUTING_KEY,
        auto_delete=True
    )

    async for message in queue:
        async with message.process():
            track = json.loads(message.body)

            await track_lyric_flow(db, track)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())

    logger.info('start consume, to exit press CTRL+C')
    
    loop.run_forever()

