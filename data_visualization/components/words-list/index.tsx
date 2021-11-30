import clsx from 'clsx'
import { motion } from 'framer-motion'
import { FC } from 'react'
import styles from './words-list.module.css'


export enum Type {
    Row,
    Column
}

export type WordsListProps = {
    type: Type,
    words: string[]
}

export const WordsList: FC<WordsListProps> = ({ words, type }) => {
    return (
        <div
            className={clsx(styles.wordList,
                type === Type.Row && styles.wordListRow,
                type === Type.Column && styles.wordListColumn
            )}
        >
            {words.map(word =>
                <motion.span
                    key={word}
                >
                    {word}
                </motion.span>
            )}
        </div>
    )
}
