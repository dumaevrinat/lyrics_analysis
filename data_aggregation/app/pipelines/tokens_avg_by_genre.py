tokens_avg_by_genre = [
    {'$group': {
        '_id': {
            'id': '$_id._id',
            'genre': {'$first': '$track.albums.genre'}
        },
        'count': {'$sum': '$count'}
    }},

    {'$group': {
        '_id': '$_id.genre',
        'avg': {'$avg': '$count'}
    }}
]
