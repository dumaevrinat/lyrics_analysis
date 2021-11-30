import { ChangeEvent, FC, useState } from 'react'
import { Chart } from 'components/chart'
import { Radio } from 'components/radio'
import { Section } from 'components/section'
import { RadioGroup } from 'components/radio-group'
import { WordsGroups } from 'components/words-groups'
import { genreConverter, getWordsGroupsDataByGenre, getWordsGroupsGenres } from 'data/transform'
import { Genre } from 'types'


export const TypicalWordsPoses: FC = () => {
    const genres = getWordsGroupsGenres()
    const [currentGenre, setCurrentGenre] = useState(genres[0])

    const wordsGroupsData = getWordsGroupsDataByGenre(currentGenre as Genre)

    const handleChangeGenre = (e: ChangeEvent<HTMLInputElement>) => {
        setCurrentGenre(e.target.value)
    }

    return (
        <Section title='Характерные слова: части речи'>
            <p className='max-w-1000'>
                Найдем самые характерные слова для каждой части речи.
                Для это отфильтруем слова, которые соответствуют основным частям речи,
                и отсортируем по их характерности для данной части речи.
            </p>

            <Chart>
                <RadioGroup>
                    {genres.map(genre =>
                        <Radio
                            id={`typical ${genre}`}
                            key={genre}
                            value={genre}
                            onChange={handleChangeGenre}
                            checked={genre === currentGenre}
                        >
                            {genreConverter[genre as Genre]}
                        </Radio>
                    )}
                </RadioGroup>

                <WordsGroups groups={wordsGroupsData} />
            </Chart>
        </Section>
    )
}
