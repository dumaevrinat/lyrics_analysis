import clsx from 'clsx'
import { FC, ReactNode } from 'react'
import styles from './chart.module.css'


export type ChartProps = {
    className?: string,
    children: ReactNode
}

export const Chart: FC<ChartProps> = ({ children, className }) => {
    return (
        <div className={clsx(styles.chart, className && className)}>
            {children}
        </div>
    )
}
