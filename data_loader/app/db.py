from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCursor
import config


client = AsyncIOMotorClient(config.MONGO_URL)
db = client[config.DATABASE_NAME]


class Database:
    def __init__(
        self,
        client: AsyncIOMotorClient,
        database: str,
        tracks_collection: str,
    ):
        self.database = client[database]
        self.tracks_collection = self.database[tracks_collection]


    def tracks_with_lyric(self) -> AsyncIOMotorCursor:
        return self.tracks_collection.find(
            {'lyric': {'$not': {'$size': 0}}},
            {'_id': True, 'lyric': True}
        )
