import { FC, ReactNode } from 'react'
import styles from './circle-counters.module.css'


type CircleCountersProps = {
    children: ReactNode
}

export const CircleCounters: FC<CircleCountersProps> = ({ children }) => {
    return (
        <div className={styles.counters}>
            {children}
        </div>
    )
}
