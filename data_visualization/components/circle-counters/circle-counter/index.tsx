import { FC } from 'react'
import { CirclesGroup, CirclesGroupProps } from '../circles-group'
import styles from './circle-counter.module.css'


export type CircleCounterProps = {
    title: string,
    total: number,
    circlesGroups: CirclesGroupProps[]
}

export const CircleCounter: FC<CircleCounterProps> = ({ title, total, circlesGroups }) => {
    return (
        <>
            <div className={styles.titleContainer}>
                <span className={styles.title}>
                    {title}
                </span>
                <span className={styles.value}>
                    {Math.floor(total)}
                </span>
            </div>

            <div className={styles.circles}>
                {circlesGroups.map((group, index) =>
                    <CirclesGroup
                        key={index}
                        count={group.count} 
                        color={group.color} 
                    />
                )}
            </div>
        </>
    )
}
