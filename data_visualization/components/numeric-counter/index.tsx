import { FC } from 'react'
import { uniqueValues } from 'utils/array'
import { Chip } from 'components/chip'
import { CategoryValues } from './category-values/category-values'
import { Label } from './label/label'
import styles from './numeric-counter.module.css'
import { Chart } from 'components/chart'


export type NumericData = {
    value: number,
    label: string,
    category: string
}

export type NumericCounterProps = {
    data: NumericData[],
    colors: string[]
}

export const NumericCounter: FC<NumericCounterProps> = ({ data, colors }) => {
    const categories = uniqueValues(data, numericData => numericData.category)
    const labels = uniqueValues(data, numericData => numericData.label)

    return (
        <Chart>
            <div className={styles.categories}>
                {categories.map((category, index) =>
                    <Chip
                        className={styles.category}
                        key={category}
                        title={category}
                        color={colors[index]}
                    />
                )}
            </div>

            <div className={styles.data}>
                <div className={styles.labels}>
                    {labels.map(label =>
                        <Label
                            key={label}
                            label={label}
                        />
                    )}
                </div>

                <div className={styles.dataColumns}>
                    {categories.map((category, index) =>
                        <CategoryValues
                            key={category}
                            color={colors[index]}
                            values={data
                                .filter(numericData => numericData.category === category)
                                .map(numericData => numericData.value)
                            }
                        />
                    )}
                </div>
            </div>
        </Chart>
    )
}
