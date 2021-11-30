import { FC } from 'react'
import styles from './category-values.module.css'


export type CategoryValuesProps = {
    values: number[],
    color: string,
}

export const CategoryValues: FC<CategoryValuesProps> = ({ values, color }) => {
    const valueStyle = {
        color: color
    }

    return (
        <div className={styles.categoryValues}>
            {values.map((value, index) =>
                <span
                    key={index}
                    className={styles.value}
                    style={valueStyle}
                >
                    {Math.floor(value)}
                </span>
            )}
        </div>
    )
}
