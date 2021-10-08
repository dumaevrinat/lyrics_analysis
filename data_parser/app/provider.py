from typing import Dict, Mapping, Optional, Union
import aiohttp
import logging

logger = logging.getLogger(__name__)


class DataProvider:
    def __init__(
        self,
        base_url: str = 'https://music.yandex.ru',
        proxy: str = None,
        lang: str = 'ru'
    ):
        self.base_url = base_url
        self.proxy = proxy or ''
        self.lang = lang

    async def _get(self, url: str, params: Mapping[str, str], timeout: Union[float, int] = 10) -> Optional[Dict]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=timeout, proxy=self.proxy) as response:
                if response.ok:
                    logger.info(f'Success {url} {params}')
                    return await response.json()
                else:
                    logger.warning(f'Failure {url} {response.status} {params} {await response.text()}')

    async def get_track(self, track: str):
        url = f'{self.base_url}/handlers/track.jsx'
        params = {
            'track': track,
            'lang': self.lang
        }

        return await self._get(url, params)
