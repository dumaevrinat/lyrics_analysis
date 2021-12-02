import { ChangeEvent, FC, useState } from 'react'
import { RadioGroup } from 'components/radio-group'
import { Section } from 'components/section'
import { Radio } from 'components/radio'
import { WordsEpoch } from 'components/words-epoch'
import { Type, WordsList } from 'components/words-list'
import { getWordsEpochsData, getWordsEpochsGenres } from 'data/transform'
import { Genre } from 'types'
import styles from './epochs.module.css'
import { Chart } from 'components/chart'
import { genreConverter } from 'data/converters'


export const Epochs: FC = () => {
    const genres = getWordsEpochsGenres()
    const [currentGenre, setCurrentGenre] = useState(genres[0])

    const wordsEpochsData = getWordsEpochsData(currentGenre as Genre)

    const handleChangeGenre = (e: ChangeEvent<HTMLInputElement>) => {
        setCurrentGenre(e.target.value)
    }

    return (
        <Section title='Эпохи'>
            <p className='max-w-1000'>
                Разделим даты выхода треков на несколько периодов и найдем самые характерные слова для каждой эпохи —
                слова, которые употреблялись в этот период чаще, чем в другие.
            </p>

            <Chart>
                <RadioGroup>
                    {genres.map(genre =>
                        <Radio
                            id={`epoch ${genre}`}
                            key={genre}
                            value={genre}
                            onChange={handleChangeGenre}
                            checked={genre === currentGenre}
                        >
                            {genreConverter[genre as Genre]}
                        </Radio>
                    )}
                </RadioGroup>

                <div className={styles.wordsEpochs}>
                    {wordsEpochsData.map(wordsEpochData =>
                        <WordsEpoch
                            key={wordsEpochData.start}
                            start={wordsEpochData.start}
                            end={wordsEpochData.end}
                        >
                            <WordsList type={Type.Column} words={wordsEpochData.words} />
                        </WordsEpoch>
                    )}
                </div>
            </Chart>
        </Section>
    )
}
