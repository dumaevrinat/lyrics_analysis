import { FC, ReactNode } from 'react'
import styles from './distribution.module.css'


export type DistributionProps = {
    children: ReactNode
}

export const Distribution: FC<DistributionProps> = ({ children }) => {
    return (
        <div className={styles.distribution}>
            {children}
        </div>
    )
}
