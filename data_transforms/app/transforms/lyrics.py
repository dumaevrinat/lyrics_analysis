from typing import Dict
from returns.pipeline import flow
from returns.curry import curry
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()

embedding = NewsEmbedding()
morph_tagger = NewsMorphTagger(embedding)


def create_doc(text: str) -> Doc:
    return Doc(text)


def segment(doc: Doc) -> Doc:
    doc.segment(segmenter)

    return doc


def morph(doc: Doc) -> Doc:
    doc.tag_morph(morph_tagger)

    return doc


def filter_tokens(doc: Doc) -> Doc:
    doc.tokens = list(filter(lambda token: token.pos != 'X' and token.pos != 'PUNCT', doc.tokens))

    return doc


def lemmatize(doc: Doc) -> Doc:
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    
    return doc


@curry
def to_dict(id: str, doc: Doc) -> Doc:
    return flow(
        doc,
        lambda doc: doc.as_json,
        lambda doc: {
            '_id': id,
            'tokens': doc.get('tokens')
        }        
    )


@curry
def lyric_pipeline(id: str, text: str) -> Dict:
    return flow(
        text,
        create_doc,
        segment,
        morph,
        filter_tokens,
        lemmatize,
        to_dict(id)
    )
