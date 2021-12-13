from typing import Dict, List, Set
from graphviz import Graph
from returns.pipeline import flow
from returns.curry import curry, partial


def create_graph(name: str) -> Graph:
    return Graph(name)


@curry
def add_node(artist: Dict, graph: Graph) -> Graph:
    id = artist.get('_id')
    name = artist.get('artist').get('name')
    genres = artist.get('artist').get('genres')

    graph.node(str(id), name, genre=genres[0])

    return graph


@curry
def add_edges(artist_id: int, similar_ids: List[int], graph: Graph) -> Graph:
    for similar_id in similar_ids:
        graph.edge(str(artist_id), str(similar_id))
    
    return graph


@curry
def get_existing_similar_ids(artists_ids: List[int], similar_artists: List[Dict]) -> Set[int]:
    return flow(
        similar_artists,
        partial(map, lambda artist: artist.get('id')),
        set,
        partial(set.intersection, artists_ids)
    )


def get_artists_ids(artists: List[Dict]) -> Set[int]:
    return flow(
        artists,
        partial(map, lambda artist: artist.get('_id')),
        partial(map, int),
        set
    )


def add_artist_to_graph(artist: Dict, similar_ids: List[int], graph: Graph) -> Graph:
    if len(similar_ids) < 1:
        return graph

    return flow(
        graph,
        add_node(artist),
        add_edges(artist.get('_id'), similar_ids)
    )


def create_artists_graph(graph_name: str, artists: List[Dict]) -> Graph:
    graph = create_graph(graph_name)

    artists_ids = get_artists_ids(artists)
    
    for artist in artists:
        similar_ids = flow(
            artist.get('allSimilar'),
            get_existing_similar_ids(artists_ids)
        )

        add_artist_to_graph(artist, similar_ids, graph)

    return graph
