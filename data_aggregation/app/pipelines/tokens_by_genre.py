tokens_by_genre = [
    {'$group': {
        '_id': {
            'lemma': '$_id.lemma',
            'genre':  {'$first': '$track.albums.genre'}
        },

        'count': {'$sum': 1}
    }},
    
    {'$group': {
        '_id': '$_id.lemma',
        'total_count': {
            '$avg': '$count'
        },
        'counts': {
            '$push': {
                'genre': '$_id.genre',
                'count': '$count'
            }
        }
    }},

    {'$unwind': '$counts'},

    {'$project': {
        '_id': 1,
        'total_count': 1,
        'counts': {
            'base_count': '$counts.count',
            'count': {
                '$divide': ['$counts.count', '$total_count']
            },
            'genre': '$counts.genre'
        }
    }},

    # {'$match': {
    #     'counts.count': {'$lte': 0.999},
    #     'counts.base_count': {'$gte': 50}
    # }},

    {'$sort': {'counts.count': -1}},

    {'$group': {
        '_id': '$counts.genre',
        'tokens': {
            '$push': {
                'lemma': '$_id',
                'count': '$counts.count',
                'base_count': '$counts.base_count'
            }
        }
    }},

    {'$project': {
        '_id': 1,
        'tokens': {'$slice': ['$tokens', 20]}
    }}
]
