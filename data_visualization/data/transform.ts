import { Genre, Pos, Phrase } from '../types'
import { uniqueValues } from '../utils/array'
import data from './on_base_coll_data.json'

export type GenreConverter = { [genre in Genre]: string}
export type PosConverter = { [pos in Pos]: Phrase}

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
    }
}

const compareGenresFn = (a: string, b: string) => b.length - a.length 

export const getCircleCountersData = () => 
    data.tokens_avg_by_genre
        .sort((a, b) => b.avg - a.avg)
        .map(raw => ({
            title: genreConverter[raw._id as Genre],
            count: raw.avg
        }))


export const getUniqueWordsDistributionGenres = () => 
    uniqueValues(data.tokens_avg_by_genre_artist, raw => raw._id)
        .sort(compareGenresFn)


export const getUniqueWordsDistribution = (genre: Genre) => {
    const sortedPeriods = data.tokens_avg_by_genre_artist
        .find(raw => raw._id === genre)?.periods
        .sort((a, b) => a.id - b.id)
    
    if (sortedPeriods) {
        const artists = sortedPeriods[sortedPeriods.length - 1].artists
        const maxValue = artists[artists.length - 1].avg
        
        return sortedPeriods.map((raw, index) => ({
            min: raw.id,
            max: sortedPeriods[index + 1]?.id || maxValue,
            items: raw.artists
                .map(artist => ({
                    value: artist.avg,
                    label: artist.name
                }))
        }))
    }
}


export const getNumericCounterData = (poses: Pos[]) => 
    data.tokens_avg_by_genre_pos
        .filter(raw => poses.indexOf(raw._id.pos as Pos) != -1)
        .map(raw => ({
            value: raw.avg,
            label: genreConverter[raw._id.genre as Genre],
            category: posConverter[raw._id.pos as Pos].plural
        }))


export const getWordsListsData = () => 
    data.tokens_by_genre
        .map(wordListData => ({
            title: genreConverter[wordListData._id as Genre],
            words: wordListData.tokens.map(token => token.lemma)
        }))
        .sort((a, b) => compareGenresFn(b.title, a.title))


export const getWordsGroupsGenres = () => 
    uniqueValues(data.tokens_avg_by_genre, raw => raw._id)
        .sort(compareGenresFn)


export const getWordsGroupsDataByGenre = (genre: Genre) => 
    data.tokens_by_genre_pos
        .filter(raw => raw._id.genre === genre)
        .sort((a, b) => a._id.pos > b._id.pos && 1 || -1)
        .map(raw => ({
            label: posConverter[raw._id.pos as Pos].plural,
            words: raw.tokens.map(token => token.lemma).slice(0, 5)
        }))


export const getWordsEpochsGenres = () => 
    uniqueValues(data.tokens_by_genre_year, data => data._id.genre)
        .sort(compareGenresFn)


export const getWordsEpochsData = (genre: Genre) => 
    data.tokens_by_genre_year
        .filter(raw => raw._id.genre === genre)
        .sort((a, b) => a._id.year.start - b._id.year.start)
        .map(raw => ({
            start: raw._id.year.start,
            end: raw._id.year.end,
            words: raw.tokens.map(token => token.lemma)
        }))
