import { Genre, Phrase, Pos } from 'types'


export type GenreConverter = { [genre in Genre]: string }
export type PosConverter = { [pos in Pos]: Phrase }
export type PosToColor = { [pos in Pos]: string }

export const genreConverter: GenreConverter = {
    'rusrap': 'хип-хоп',
    'rusestrada': 'эстрада',
    'rusrock': 'рок',
    'other': 'другие жанры',
    'ruspop': 'поп-музыка'
}

export const posConverter: PosConverter = {
    'NOUN': {
        singular: 'существительное',
        plural: 'существительные'
    },
    'VERB': {
        singular: 'глагол',
        plural: 'глаголы'
    },
    'ADJ': {
        singular: 'прилагательное',
        plural: 'прилагательные'
    },
    'ADV': {
        singular: 'наречие',
        plural: 'наречия'
    },
    'PRON': {
        singular: 'местоимение',
        plural: 'местоимения'
    },
    'OTHER': {
        singular: 'другая часть речи',
        plural: 'другие'
    }
}

export const posToColor: PosToColor = {
    'ADJ': '#0018FF',
    'ADV': '#1480FE',
    'NOUN': '#27D9FE',
    'OTHER': '#3BFDD7',
    'PRON': '#40FDCC',
    'VERB': '#4EFD9A',
}
