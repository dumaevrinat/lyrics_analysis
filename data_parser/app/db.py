from typing import Dict, Iterable, List
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from pymongo.operations import UpdateOne


class Database:
    def __init__(
        self,
        client: AsyncIOMotorClient,
        database: str,
        artists_collection: str,
        artists_info_collection: str,
        tracks_collection: str
    ):
        self.database = client[database]
        self.artists_collection = self.database[artists_collection]
        self.tracks_collection = self.database[tracks_collection]
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

    async def insert_artist_info(self, artist_info: Dict):
        artist_info['_id'] = artist_info.get('artist').get('id')

        return await self._insert_one(self.artists_info_collection, artist_info)

    async def insert_artist(self, artist: Dict):
        artist['_id'] = artist.get('artist').get('id')

        return await self._insert_one(self.artists_collection, artist)

    async def insert_artists(self, artists: Iterable[Dict]):
        for artist in artists:
            artist['_id'] = artist.get('artist').get('id')

        return await self._insert_many(self.artists_collection, artists)

    async def insert_track(self, track: Dict):
        track['_id'] = track.get('track').get('id')

        return await self._insert_one(self.tracks_collection, track)

    async def insert_tracks(self, tracks: Iterable[Dict]):
        for track in tracks:
            track['_id'] = track.get('track').get('id')

        return await self._insert_many(self.tracks_collection, tracks)
