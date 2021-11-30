from argparse import ArgumentParser
import asyncio
import logging
import config
import json
import pipelines
from motor.motor_asyncio import AsyncIOMotorClient


logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)


async def main(file: str):
    client = AsyncIOMotorClient(config.MONGO_URL)
    base_pipeline_collection = client[config.DATABASE_NAME][config.BASE_PIPELINE_COLLECTION_NAME]

    logger.info('start pipeline')

    async for doc in base_pipeline_collection.aggregate(pipelines.main_pipeline, allowDiskUse=True):
        with open(file, 'w', encoding='utf8') as fp:
            json.dump(doc, fp, ensure_ascii=False)

    logger.info('end pipeline')


if __name__ == '__main__':
    parser = ArgumentParser(description='Aggregate data from mongodb to json file')
    
    parser.add_argument('file', type=str, help='json file')
    
    args = parser.parse_args()

    asyncio.run(main(args.file))
