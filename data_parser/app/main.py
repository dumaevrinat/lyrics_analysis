import logging
import asyncio
from typing import Callable, Coroutine, List, TypeVar
from provider import DataProvider


T = TypeVar('T')


def create_tasks(
    func: Callable[[T], Coroutine],
    items: List[T]
):
    return list(map(lambda item: asyncio.create_task(func(item)), items))


async def parse_tracks(provider: DataProvider, tracks: List[str]):
    tasks = create_tasks(provider.get_track, tracks)

    tracks_info = await asyncio.gather(*tasks)

    for track_info in tracks_info:
        print(track_info.get('track').get('title'))


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')

    tracks = ['91670733', '83063895', '89179753', '89179904', '89179910', '89179914', '89179916']
    provider = DataProvider()

    asyncio.run(parse_tracks(provider, tracks))


if __name__ == '__main__':
    main()
