import { ChangeEvent, FC, useState } from 'react'
import { Section } from 'components/section'
import { getUniqueWordsDistribution, getUniqueWordsDistributionGenres } from 'data/transform'
import { Genre } from 'types'
import { Distribution } from 'components/distribution'
import { DistributionRange } from 'components/distribution/distribution-range'
import { RadioGroup } from 'components/radio-group'
import { Radio } from 'components/radio'
import { Chart } from 'components/chart'
import { genreConverter } from 'data/converters'


export const UniqueWordsArtists: FC = () => {
    const genres = getUniqueWordsDistributionGenres()
    const [currentGenre, setCurrentGenre] = useState(genres[0])

    const distributionData = getUniqueWordsDistribution(currentGenre as Genre)

    const handleChangeGenre = (e: ChangeEvent<HTMLInputElement>) => {
        setCurrentGenre(e.target.value)
    }

    return (
        <Section title='Уникальные слова: исполнители'>
            <p className='max-w-1000'>
                Для получения топа исполнителей с наибольшим количеством уникальных слов рассмотрим
                только самых популярных артистов по&nbsp;количеству лайков и отсортируем их.
            </p>

            <Chart>
                <RadioGroup>
                    {genres.map(genre =>
                        <Radio
                            id={`distribution ${genre}`}
                            key={genre}
                            value={genre}
                            onChange={handleChangeGenre}
                            checked={genre === currentGenre}
                        >
                            {genreConverter[genre as Genre]}
                        </Radio>
                    )}
                </RadioGroup>

                <Distribution>
                    {distributionData?.map(rangeData =>
                        <DistributionRange
                            key={rangeData.items[0].label}
                            min={rangeData.min}
                            max={rangeData.max}
                            items={rangeData.items}
                        />
                    )}
                </Distribution>
            </Chart>
        </Section>
    )
}
