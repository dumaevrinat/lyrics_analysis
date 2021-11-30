import { FC } from 'react'
import { Chip } from 'components/chip'
import { Section } from 'components/section'
import { Type, WordsList } from 'components/words-list'
import { getWordsListsData } from 'data/transform'
import styles from './typical-words-genres.module.css'
import { motion, Variants } from 'framer-motion'


const wordsListVariants: Variants = {
    initial: {
        y: 20,
        opacity: 0
    },
    onscreen: {
        y: 0,
        opacity: 1,
        transition: {
            type: "spring",
            bounce: 0,
            duration: 0.8
        }
    }
}

export const TypicalWordsGenres: FC = () => {
    const wordsListsData = getWordsListsData()

    return (
        <Section title='Характерные слова'>
            <p className='max-w-1000'>
                Определим самые характерные слова для разных жанров.
            </p>
            
            <p className='max-w-1000'>
                Для этого рассчитаем как часто слово встречается в данном жанре и во всех остальных жанрах.
                Делим данные частотности, сортируем значения и получаем характерные слова.
            </p>

            <div className={styles.wordsLists}>
                {wordsListsData.map(wordsListData =>
                    <motion.div
                        key={wordsListData.title}
                        className={styles.wordsListContainer}
                        initial='initial'
                        whileInView='onscreen'
                        viewport={{ once: false, amount: 0.6 }}
                    >
                        <motion.div
                            className={styles.wordsList}
                            variants={wordsListVariants}
                        >
                            <Chip
                                title={wordsListData.title}
                            />
                            <WordsList
                                type={Type.Row}
                                words={wordsListData.words}
                            />
                        </motion.div>
                    </motion.div>
                )}
            </div>
        </Section>
    )
}
