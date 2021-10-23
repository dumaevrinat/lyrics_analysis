import asyncio
import logging
from typing import Callable, Dict, Iterable, Optional
from asyncio import IncompleteReadError, TimeoutError
from aiohttp.client import ClientSession
from aiohttp_socks import ProxyError, ProxyTimeoutError, ProxyConnectionError
from aiohttp.client_exceptions import ClientError
from providers import DataProvider


logger = logging.getLogger(__name__)


class Parser:
    def __init__(self, session: ClientSession):
        self.session = session
        self.data_provider = DataProvider(session)
        
    async def catch_parse(self, parse_func: Callable, retry: bool, *args, **kwargs):
        try:
            return await parse_func(self, *args, **kwargs)
        except (
            TimeoutError,
            ClientError, 
            ConnectionError, 
            ProxyError, 
            ProxyTimeoutError, 
            ProxyConnectionError, 
            IncompleteReadError
        ) as e:
            logger.warning(f'{e.__class__.__name__} {e} {parse_func.__name__} {args}')

            if retry:
                self.catch_parse(parse_func, True, *args, **kwargs)

    def catch_parse_decorator(retry: bool):
        def decorator(parse_func: Callable):
            async def wrapper(self: 'Parser', *args, **kwargs):
                return await self.catch_parse(parse_func, retry, *args, **kwargs)
            
            return wrapper
        
        return decorator

    @catch_parse_decorator(retry=True)
    async def parse_track(self, track_id: str) -> Optional[Dict]:
        return await self.data_provider.track(track_id)
        
    @catch_parse_decorator(retry=False)
    async def parse_tracks_from_artist(self, artist_id: str) -> Optional[Iterable[Dict]]:
        artist = await self.data_provider.artist(artist_id, what='tracks')

        if artist:
            track_ids = artist.get('trackIds')
            
            track_infos = await asyncio.gather(
                *[self.parse_track(track_id) for track_id in track_ids]
            )

            return [track_info for track_info in track_infos if track_info is not None]
    
    @catch_parse_decorator(retry=True)
    async def parse_artist_info(self, artist_id: str) -> Optional[Dict]:
        return await self.data_provider.artist(artist_id, what='info')

    @catch_parse_decorator(retry=False)
    async def parse_artists_from_metatag(self, metatag_id: str, page: int) -> Iterable[Optional[Dict]]:
        metatag_data = await self.data_provider.metatag(metatag_id, 'artists', page)

        if metatag_data:
            return metatag_data.get('metatag').get('artists')

    @catch_parse_decorator(retry=False)
    async def parse_all_artists_from_metatag(self, metatag_id: str) -> Iterable[Optional[Dict]]:
        metatag_data = await self.data_provider.metatag(metatag_id, 'artists')

        if metatag_data:
            pager = metatag_data.get('metatag').get('pager')
            pages_count = min(pager.get('total') // 100 + 1, 101)

            artists = await asyncio.gather(
                *[self.parse_artists_from_metatag(metatag_id, page) for page in range(pages_count)]
            )

            return [artist for page_artists in artists for artist in page_artists]

