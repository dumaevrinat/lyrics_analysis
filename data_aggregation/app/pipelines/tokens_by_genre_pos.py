tokens_by_genre_pos = [
    {'$group': {
        '_id': {
            'lemma': '$_id.lemma',
            'pos': '$_id.pos',
            'genre':  {'$first': '$track.albums.genre'}
        },

        'count': {'$sum': 1}
    }},
    
    {'$group': {
        '_id': '$_id.lemma',
        'total_count': {
            '$sum': '$count'
        },
        'counts': {
            '$push': {
                'genre': '$_id.genre',
                'pos': '$_id.pos',
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
            'genre': '$counts.genre',
            'pos': '$counts.pos'
        }
    }},


    {'$match': {
        'counts.count': {'$lte': 0.999},
        'counts.base_count': {'$gte': 15}
    }},

    {'$sort': {'counts.count': -1}},

    {'$group': {
        '_id': {
            'genre': '$counts.genre',
            'pos': '$counts.pos'
        },
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
        'tokens': {'$slice': ['$tokens', 10]}
    }}
]
