from .base_pipeline import base_pipeline, filter_token_pos_base, filter_token_pos, filter_token_lemma
from .tokens_by_genre import tokens_by_genre
from .tokens_by_genre_pos import tokens_by_genre_pos
from .tokens_by_genre_year import tokens_by_genre_year
from .tokens_avg_by_genre import tokens_avg_by_genre
from .tokens_avg_by_genre_pos import tokens_avg_by_genre_pos
from .tokens_avg_by_genre_artist import tokens_avg_by_genre_artist


main_pipeline = base_pipeline + [
    {'$facet': {
        'tokens_by_genre': filter_token_pos + filter_token_lemma + tokens_by_genre,
        'tokens_by_genre_pos': filter_token_pos + filter_token_lemma + tokens_by_genre_pos,
        'tokens_by_genre_year': filter_token_pos + filter_token_lemma + tokens_by_genre_year,
        'tokens_avg_by_genre': filter_token_pos_base + tokens_avg_by_genre,
        'tokens_avg_by_genre_pos': filter_token_pos_base + tokens_avg_by_genre_pos,
        'tokens_avg_by_genre_artist': filter_token_pos_base + tokens_avg_by_genre_artist
    }}
]
