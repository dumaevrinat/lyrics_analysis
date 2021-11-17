tokens_by_genre_year = [
    {'$set': {
        'year': {
            '$switch': {
                'branches': [
                    {
                        'case': {'$and': [
                            {'$gte': [{'$first': '$track.albums.year'}, 1990]},
                            {'$lt': [{'$first': '$track.albums.year'}, 2000]}
                        ]},
                        'then': 1990
                    },
                    {
                        'case': {'$and': [
                            {'$gte': [{'$first': '$track.albums.year'}, 2000]},
                            {'$lt': [{'$first': '$track.albums.year'}, 2010]}
                        ]},
                        'then': 2000
                    },
                    {
                        'case': {'$and': [
                            {'$gte': [{'$first': '$track.albums.year'}, 2010]},
                            {'$lt': [{'$first': '$track.albums.year'}, 2015]}
                        ]},
                        'then': 2010
                    },
                    {
                        'case': {'$gte': [{'$first': '$track.albums.year'}, 2015]},
                        'then': 2015
                    }
                ],
                'default': 'other'
            }
        }
    }},

    {'$group': {
        '_id': {
            'lemma': '$_id.lemma',
            'genre': {'$first': '$track.albums.genre'},
            'year': '$year'
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
                'year': '$_id.year',
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
            'year': '$counts.year'
        }
    }},

    # {'$match': {
    #     'counts.count': {'$lte': 0.999},
    #     'counts.base_count': {'$gte': 20}
    # }},

    {'$sort': {'counts.count': -1}},

    {'$group': {
        '_id': {
            'genre': '$counts.genre',
            'year': '$counts.year'
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
        'tokens': {'$slice': ['$tokens', 15]}
    }}
]
