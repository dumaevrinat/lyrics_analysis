tokens_avg_by_genre_pos = [
    {'$set': {
        '_id.pos': {
            '$cond': { 
                'if': { 
                    '$in': ['$_id.pos', ['ADJ', 'ADV', 'NOUN', 'VERB']] 
                }, 
                'then': '$_id.pos', 'else': 'OTHER' 
            }
        }
    }},
    
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

    {'$sort': {'_id.pos': 1}},

    {'$group': {
        '_id': '$_id.genre',
        'poses': {
            '$push': {
                'pos': '$_id.pos',
                'avg': '$avg'
            }
        }
    }},
]
