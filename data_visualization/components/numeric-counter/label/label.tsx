import { FC } from 'react'
import styles from './label.module.css'


export type LabelProps = {
    label: string
}

export const Label: FC<LabelProps> = ({ label }) => {
    return (
        <div className={styles.container}>
            <span
                key={label} 
                className={styles.label}
            >
                {label}
            </span>
        </div>
    )
}
