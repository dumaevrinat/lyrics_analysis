from typing import Optional
from typing_extensions import Literal

from aiohttp.client import ClientSession

from .base_provider import BaseProvider


class DataProvider(BaseProvider):
    def __init__(
        self,
        session: ClientSession,
        base_url: str = 'https://music.yandex.ru',
        lang: str = 'ru'
    ):
        super().__init__(session, base_url)
        self.lang = lang
    
    async def main(
        self,
        what: Literal['genre', 'chart', 'new-releases', 'home']
    ):
        url = f'{self.base_url}/handlers/main.jsx'

        params = {
            'what': what,
            'lang': self.lang
        }

        return await self._get(url, params)

    async def metatag(
        self, 
        id: str, 
        tab: Literal['artists', 'albums', 'playlists', None], 
        page: int = None, 
        sort_by: str = None
    ):
        url = f'{self.base_url}/handlers/metatag.jsx'

        params = {
            'id': id,
            'tab': tab or '',
            'page': page or '',
            'sortBy': sort_by or '',
            'lang': self.lang
        }

        return await self._get(url, params)

    async def artist(
        self, 
        artist: str, 
        what: Literal['tracks', 'albums', 'videos', 'info', None], 
        sort: str = None
    ):
        url = f'{self.base_url}/handlers/artist.jsx'

        params = {
            'artist': artist,
            'what': what or '',
            'sort': sort or '',
            'lang': self.lang
        }

        return await self._get(url, params)

    async def track(
        self, 
        track: str
    ):
        url = f'{self.base_url}/handlers/track.jsx'

        params = {
            'track': track,
            'lang': self.lang
        }

        return await self._get(url, params)

    async def album_with_track_lyric(
        self,
        track: str,
        album: Optional[str] = None
    ):
        url = f'{self.base_url}/handlers/album.jsx'
        
        params = {
            'album': album or '',
            'currentTrackId': track,
            'byTrack': track,
            'lang': self.lang
        }

        return await self._get(url, params)
