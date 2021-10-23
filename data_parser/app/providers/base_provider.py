from typing import Dict, Mapping, Optional, Union
import logging
from aiohttp.client import ClientSession


logger = logging.getLogger(__name__)


class BaseProvider:
    def __init__(
        self,
        session: ClientSession,
        base_url: str
    ):
        self.session = session
        self.base_url = base_url

    async def _get(
        self,
        url: str,
        params: Optional[Mapping[str, str]] = None,
        timeout: Union[float, int] = 15,
        content_type: Optional[str] = 'application/json'
    ) -> Optional[Dict]:
        async with self.session.get(url, params=params, timeout=timeout, ssl=False) as response:
            if response.ok:
                logger.info(f'Success {url} {params}')
                return await response.json(content_type=content_type)
            else:
                response.raise_for_status()
