import { FC } from 'react'
import { Section } from 'components/section'
import { NumericCounter } from 'components/numeric-counter'
import { getNumericCounterData } from 'data/transform'
import { Pos } from 'types'


export const UniqueWordsPoses: FC = () => {
    const poses: Pos[] = ['NOUN', 'VERB', 'ADJ', 'ADV', 'PRON']
    const colors = ['#0018FF', '#147DFE', '#27D4FE', '#3BFDDE', '#4EFDA2']

    const numericCounterData = getNumericCounterData(poses)

    return (
        <Section title='Уникальные слова: части речи'>
            <p className='max-w-1000'>
                Посчитаем количество уникальныx слов в одном треке отдельно для каждой части речи.
            </p>

            <NumericCounter
                data={numericCounterData}
                colors={colors}
            />
        </Section>
    )
}
