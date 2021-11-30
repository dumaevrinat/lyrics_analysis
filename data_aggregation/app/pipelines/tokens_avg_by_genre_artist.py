tokens_avg_by_genre_artist = [
    {'$unwind': '$track.artists'},

    {'$unwind': '$track.albums'},

    {'$set': {
        'track.genre': {
            '$switch': {
                'branches': [
                    {
                        'case': {'$eq': [{'$first': '$track.artists.genres'}, 'rusrap']},
                        'then': 'rusrap'
                    },
                    {
                        'case': {'$eq': [{'$first': '$track.artists.genres'}, 'ruspop']},
                        'then': 'ruspop'
                    },
                    {
                        'case': {'$eq': [{'$first': '$track.artists.genres'}, 'rusestrada']},
                        'then': 'rusestrada'
                    },
                    {
                        'case': {'$eq': [{'$first': '$track.artists.genres'}, 'rusrock']},
                        'then': 'rusrock'
                    }
                ],
                'default': 'other'
            }
        }
    }},

    {'$group': {
        '_id': {
            'id': '$_id._id',
            'artist': {
                'id': '$track.artists.id',
                'name': '$track.artists.name',
            },
            'genre': '$track.genre'
        },

        'likes': {'$sum': '$track.albums.likesCount'},
        'count': {'$sum': 1}
    }},

    {'$group': {
        '_id': {
            'artist': {
                'id': '$_id.artist.id',
                'name': '$_id.artist.name',
            },
            'genre': '$_id.genre'
        },
        'likes': {'$sum': '$likes'},
        'avg': {'$avg': '$count'},
        'tracks_count': {'$sum': 1}
    }},

    {'$match': {
        'tracks_count': {'$gt': 1}
    }},

    {'$sort': {'likes': -1}},

    {'$group': {
        '_id': '$_id.genre',
        'artists': {
            '$push': {
                'id': '$_id.artist.id',
                'name': '$_id.artist.name',
                'avg': '$avg'
            }
        }
    }},

    {'$project': {
        '_id': 1,
        'artists': {'$slice': ['$artists', 60]}
    }},

    {'$unwind': '$artists'},

    { '$sort': {
        'artists.avg' : -1 
    }},

    {'$bucket': {
        'groupBy': '$artists.avg',
        'boundaries': [50, 70, 100, 150, 250, 400],
        'default': 'other',
        'output': {
            'artists': {
                '$push': {
                    'id': '$artists.id',
                    'name': '$artists.name',
                    'avg': '$artists.avg',
                    'genre': '$_id'
                }
            }
        }
    }},

    {'$match': { 
        '_id' : { '$type': 'number' } 
    }},

    {'$unwind': '$artists'},

    {'$group': {
        '_id': {
            'genre': '$artists.genre',
            'period': '$_id'
        },
        'artists': {
            '$push': {
                'id': '$artists.id',
                'name': '$artists.name',
                'avg': '$artists.avg'
            }
        }
    }},

    {'$group': {
        '_id': '$_id.genre',
        'periods': {
            '$push': {
                'id': '$_id.period',
                'artists': '$artists'
            }
        }
    }},
]
