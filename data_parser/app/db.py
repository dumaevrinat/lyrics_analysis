from typing import Dict, Iterable
from motor.motor_asyncio import AsyncIOMotorClient
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

    async def insert_artist_info(self, artist_info: Dict):
        artist_info['_id'] = artist_info.get('artist').get('id')

        return await self.artists_info_collection.update_one(
            {'_id': artist_info.get('_id')},
            {'$set': artist_info},
            upsert=True
        )

    async def insert_artist(self, artist: Dict):
        artist['_id'] = artist.get('artist').get('id')

        return await self.artists_collection.update_one(
            {'_id': artist.get('_id')},
            {'$set': artist},
            upsert=True
        )

    async def insert_artists(self, artists: Iterable[Dict]):
        for artist in artists:
            artist['_id'] = artist.get('artist').get('id')

        return await self.artists_collection.bulk_write([
            UpdateOne(
                {'_id': artist.get('_id')},
                {'$set': artist},
                upsert=True
            ) for artist in artists
        ])

    async def insert_track(self, track: Dict):
        track['_id'] = track.get('track').get('id')

        return await self.tracks_collection.update_one(
            {'_id': track.get('_id')},
            {'$set': track},
            upsert=True
        )

    async def insert_tracks(self, tracks: Iterable[Dict]):
        for track in tracks:
            track['_id'] = track.get('track').get('id')

        return await self.tracks_collection.bulk_write([
            UpdateOne(
                {'_id': track.get('_id')},
                {'$set': track},
                upsert=True
            ) for track in tracks
        ])
