import logging
from motor.motor_asyncio import AsyncIOMotorClient
from db import Database
from tqdm.asyncio import tqdm
from aio_pika import connect, Message, Channel
import asyncio
import config
import json


logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)


async def send(channel: Channel, message_body: dict):
    message = Message(body=json.dumps(message_body).encode())

    await channel.default_exchange.publish(
        message, routing_key=config.QUEUE_ROUTING_KEY
    )


async def main():
    client = AsyncIOMotorClient(config.MONGO_URL)
    db = Database(
        client, 
        config.DATABASE_NAME, 
        config.TRACKS_COLLECTION_NAME
    )

    cursor = db.tracks_with_lyric()

    connection = await connect(config.QUEUE_URL)
    
    async with connection:
        channel = await connection.channel()

        logger.info('start loading tracks')

        async for track in tqdm(cursor):
            await send(channel, track)
    
        logger.info('end loading tracks')

if __name__ == '__main__':
    asyncio.run(main())
