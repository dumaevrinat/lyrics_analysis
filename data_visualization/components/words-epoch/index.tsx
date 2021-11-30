import { FC, ReactNode } from 'react'
import styles from './words-epoch.module.css'


export type WordsEpochProps = {
    start: string | number,
    end: string | number,
    children: ReactNode
}

export const WordsEpoch: FC<WordsEpochProps> = ({ start, end, children }) => {
    return (
        <div className={styles.wordsEpoch}>
            <span>
                {`${start}—${end}`}
            </span>
            {children}
        </div>
    )
}
