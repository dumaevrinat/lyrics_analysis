from typing import Dict, List, Optional
from typing_extensions import Literal

from aiohttp.client import ClientSession

from .base_provider import BaseProvider


class ProxyProvider(BaseProvider):
    def __init__(
        self, 
        session: ClientSession,
        base_url: str = 'https://proxylist.geonode.com/api',
    ):
        super().__init__(session, base_url)

    async def proxy_list(
        self, 
        filter_last_checked: Optional[int] = None, 
        filter_up_time: Optional[int] = 100, 
        speed: Optional[Literal['fast', 'medium', 'slow']] = 'fast', 
        country: Optional[str] = None,
        limit: int = 200, 
        page: int = 1, 
        sort_by: Optional[str] = 'lastChecked', 
        sort_type: Optional[str] = 'desc',
        protocols: Optional[List[Literal['http', 'https', 'socks4', 'socks5']]] = ['socks4', 'socks5']
    ):
        url = f'{self.base_url}/proxy-list'

        params = {
            'filterLastChecked': filter_last_checked or '',
            'filterUpTime': filter_up_time,
            'speed': speed or '',
            'country': country or '',
            'limit': limit,
            'page': page,
            'sort_by': sort_by or '',
            'sort_type': sort_type or '',
            'protocols': ','.join(protocols) if protocols else ''
        }

        return await self._get(url, params)
    
    async def get_ip(self):
        url = 'https://api.myip.com/'

        return await self._get(url, content_type='text/html')


def proxy_to_url(proxy: Dict) -> str:
    return f'{proxy.get("protocols")[0]}://{proxy.get("ip")}:{proxy.get("port")}'
