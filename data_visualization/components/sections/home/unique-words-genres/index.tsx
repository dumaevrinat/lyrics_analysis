import { FC } from 'react'
import { Section } from 'components/section'
import { CircleCounter } from 'components/circle-counter'
import { getCircleCountersData } from 'data/transform'
import styles from './unique-words-genres.module.css'


export const UniqueWordsGenres: FC = () => {
    const circleCountersData = getCircleCountersData()
    const max = Math.max(...circleCountersData.map(counter => counter.count))

    return (
        <Section title='Уникальные слова'>
            <p className='max-w-1000'>
                Рассмотрим среднее количество уникальных слов в одном треке для каждого жанра.
            </p>

            <div className={styles.counters}>
                {circleCountersData.map(counter =>
                    <CircleCounter
                        title={counter.title}
                        count={counter.count}
                        key={counter.title}
                        max={max}
                    />
                )}
            </div>
        </Section>
    )
}
