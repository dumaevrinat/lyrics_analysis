base_pipeline = [
    {'$unwind': '$tokens'},

    {'$set': {
        'tokens.lemma': {
            '$convert': {
                'input': '$tokens.lemma',
                'to': 'int',
                'onError': '$tokens.lemma'
            }
        }
    }},

    {'$match': {
        '$expr': {'$not': [{'$isNumber': '$tokens.lemma'}]}
    }},

    {'$group': {
        '_id': {
            '_id': '$_id', 
            'lemma': '$tokens.lemma', 
            'pos': '$tokens.pos'
        },

        'count': {'$sum': 1}
    }},

    {'$lookup': {
        'from': 'tracks', 
        'localField': '_id._id', 
        'foreignField': '_id', 
        'as': 'track_info'
    }}, 
    
    {'$unwind': '$track_info'},

    {'$match': {
        '$or': [
            {'track_info.lyric.0.textLanguage': 'ru'},
            {'track_info.lyric.0.textLanguage': {'$exists': False}}
        ]
    }},
    
    {'$project': {
        '_id': 1,
        'count': 1,
        'track': {
            'title': '$track_info.track.title',
            'artists': '$track_info.artists',
            'albums': '$track_info.track.albums'
        }
    }},

    {'$set': {
        'track.albums.genre': {
            '$switch': {
                'branches': [
                    {
                        'case': {'$eq': [{'$first': '$track.albums.genre'}, 'rusrap']},
                        'then': 'rusrap'
                    },
                    {
                        'case': {'$eq': [{'$first': '$track.albums.genre'}, 'ruspop']},
                        'then': 'ruspop'
                    },
                    {
                        'case': {'$eq': [{'$first': '$track.albums.genre'}, 'rusestrada']},
                        'then': 'rusestrada'
                    },
                    {
                        'case': {'$eq': [{'$first': '$track.albums.genre'}, 'rusrock']},
                        'then': 'rusrock'
                    }
                ],
                'default': 'other'
            }
        }
    }}
]

def merge(collection: str): 
    return [
        {'$merge': {
            'into': collection,
            'on': '_id',
            'whenMatched': 'replace', 
            'whenNotMatched': 'insert'
        }}
    ]

filter_token_pos_base = [
    {'$match': {
        '_id.pos': {
            '$not': {'$in': ['PUNCT', 'SYM', 'X']}
        }
    }}
]

filter_token_pos = [
    {'$match': {
        '_id.pos': {
            '$in': ['ADJ', 'ADV', 'NOUN', 'VERB']
        }
    }}
]

filter_token_lemma = [
    {'$match': {
        '$expr': {'$ne': [{'$strLenCP': '$_id.lemma'}, 1]}
    }}
]

filter_albums_genre = [
    {'$match': {
        'track.albums.0.genre': {
            '$in': ['rusrap', 'rusrock', 'ruspop', 'rusestrada']
        }
    }}
]
