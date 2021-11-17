from typing import Dict, List
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection, AsyncIOMotorCursor
from pymongo.operations import UpdateOne
import config


client = AsyncIOMotorClient(config.MONGO_URL)
db = client[config.DATABASE_NAME]

tracks_collection = db[config.TRACKS_COLLECTION_NAME]
artists_collection=  db[config.ARTISTS_COLLECTION_NAME]

class Database:
    def __init__(
        self,
        client: AsyncIOMotorClient,
        database: str,
        artists_collection: str,
        artists_info_collection: str,
        tracks_collection: str,
        tracks_tokens_collection: str
    ):
        self.database = client[database]
        self.artists_collection = self.database[artists_collection]
        self.tracks_collection = self.database[tracks_collection]
        self.tracks_tokens_collection = self.database[tracks_tokens_collection]
        self.artists_info_collection = self.database[artists_info_collection]

    async def _insert_one(self, collection: AsyncIOMotorCollection, document: Dict):
        return await collection.update_one(
            {'_id': document.get('_id')},
            {'$set': document},
            upsert=True
        )

    async def _insert_many(self, collection: AsyncIOMotorCollection, documents: List[Dict]):
        return await collection.bulk_write([
            UpdateOne(
                {'_id': document.get('_id')},
                {'$set': document},
                upsert=True
            ) for document in documents
        ])

    def tracks_with_lyric(self) -> AsyncIOMotorCursor:
        return self.tracks_collection.find(
            {'lyric': {'$not': {'$size': 0}}},
            {'_id': True, 'lyric': True}
        )

    def artists_with_genres(self) -> AsyncIOMotorCursor:
        return self.artists_info_collection.find(
            {'allSimilar': {'$not': {'$size': 0}}},
            {'_id': True, 'allSimilar': True, 'artist.name': True, 'artist.genres': True}
        )

    async def insert_track_with_tokens(self, track: Dict):
        return await self._insert_one(self.tracks_tokens_collection, track)