import { FC } from 'react'
import { Section } from 'components/section'
import { CircleCounters } from 'components/circle-counters'
import { getCircleCountersData } from 'data/transform'
import { CircleCounter } from 'components/circle-counters/circle-counter'


export const UniqueWordsGenres: FC = () => {
    const circleCountersData = getCircleCountersData()

    return (
        <Section title='Уникальные слова'>
            <p className='max-w-1000'>
                Для начала рассмотрим среднее количество уникальных слов в одном треке отдельно для каждого жанра.
                Уникальное слово будем обозначать одной&nbsp;ячейкой.
            </p>

            <CircleCounters>
                {circleCountersData.map(counter =>
                    <CircleCounter
                        key={counter.title} 
                        title={counter.title}
                        total={counter.count}
                        circlesGroups={[{
                            count: counter.count
                        }]}
                    />
                )}
            </CircleCounters>
        </Section>
    )
}
