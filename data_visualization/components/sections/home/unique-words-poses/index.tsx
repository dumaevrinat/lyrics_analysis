import { FC } from 'react'
import { Section } from 'components/section'
import { getNumericCounterData } from 'data/transform'
import { Genre, Pos } from 'types'
import { CircleCounters } from 'components/circle-counters'
import { CircleCounter } from 'components/circle-counters/circle-counter'
import { Chip } from 'components/chip'
import styles from './unique-words-poses.module.css'
import { genreConverter, posConverter, posToColor } from 'data/converters'


export const UniqueWordsPoses: FC = () => {
    const poses: Pos[] = ['ADJ', 'ADV', 'NOUN', 'OTHER', 'VERB']

    const numericCounterData = getNumericCounterData(poses)

    return (
        <Section title='Уникальные слова: части речи'>
            <p className='max-w-1000'>
                Посчитаем количество уникальныx слов в одном треке отдельно для каждой части речи и сгруппируем их.
            </p>

            <CircleCounters>
                {numericCounterData.map(counter =>
                    <CircleCounter
                        key={counter.genre}
                        title={genreConverter[counter.genre as Genre]}
                        total={counter.totalAvg}
                        circlesGroups={counter.poses.map(pos => ({
                            count: pos.avg,
                            color: posToColor[pos.pos as Pos]
                        }))}
                    />
                )}
            </CircleCounters>

            <div className={styles.posesChips}>
                {poses.map(pos => 
                    <Chip 
                        key={pos}
                        title={posConverter[pos as Pos].plural}
                        color={posToColor[pos]}
                    />
                )}
            </div>

        </Section>
    )
}
