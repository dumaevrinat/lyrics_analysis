import { FC } from 'react'
import styles from './circles-group.module.css'


export type CirclesGroupProps = {
    count: number,
    color?: string
}

export const CirclesGroup: FC<CirclesGroupProps> = ({ color, count }) => {
    const roundedCount = Math.floor(count)
    const circles = Array
        .from(Array(roundedCount).keys())
        .map(circle => circle + 1)

    const circleStyle = color ? {
        background: color
    } : {}

    return (
        <>
            {circles.map(circle =>
                <circle
                    className={styles.circle}
                    key={circle}
                    style={circleStyle}
                >
                    {circle === circles.length && circle}
                </circle>
            )}
        </>
    )
}
