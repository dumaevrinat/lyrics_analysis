import clsx from 'clsx'
import { AnimatePresence, motion, Variants } from 'framer-motion'
import { FC } from 'react'
import styles from './words-group.module.css'


export type WordsGroupProps = {
    className?: string,
    words: string[]
}

const wordVariants: Variants = {
    initial: {
        opacity: 0,
        y: -20
    },
    animate: index => ({
        opacity: 1,
        y: 0,
        transition: {
            delay: index * 0.03,
            bounce: 0
        }
    }),
    exit: {
        opacity: 0,
        y: 20
    }
}

export const WordsGroup: FC<WordsGroupProps> = ({ className, words }) => {
    return (
        <div className={clsx(styles.wordsGroup, className)}>
            {words.map((word, index) =>
                <AnimatePresence key={word}>
                    <motion.span
                        variants={wordVariants}
                        custom={index}
                        initial='initial'
                        animate='animate'
                        exit='exit'
                    >
                        {word}
                    </motion.span>
                </AnimatePresence>
            )}
        </div>
    )
}
