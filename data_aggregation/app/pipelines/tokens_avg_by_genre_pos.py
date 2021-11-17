tokens_avg_by_genre_pos = [
    {'$group': {
        '_id': {
            'id': '$_id._id',
            'pos': '$_id.pos',
            'genre':  {'$first': '$track.albums.genre'}
        },

        'count': {'$sum': 1}
    }},

    {'$group': {
        '_id': {
            'pos': '$_id.pos',
            'genre': '$_id.genre'
        },

        'avg': {'$avg': '$count'}
    }},

    {'$sort': {'_id.pos': 1}}
]
