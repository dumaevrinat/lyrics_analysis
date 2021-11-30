import { FC, MouseEvent } from 'react'
import { motion, Variants } from 'framer-motion'
import { scrollSmooth } from 'utils/scroll'
import styles from './intro.module.css'


const arrowVariants: Variants = {
    initial: {
        y: 0
    },
    hover: {
        y: 10,
        scale: 1.2
    },
    animate: {
        y: 15,
        scale: 1.3
    }
}

export const Intro: FC = () => {
    const handleStartClick = (e: MouseEvent<HTMLAnchorElement>) => {
        e.preventDefault()
        scrollSmooth('start')
    }
    
    return (
        <div className={styles.intro}>
            <motion.a 
                onClick={handleStartClick}
                whileHover='hover'
                whileTap='animate'
            >
                <h1>Анализ данных<br/>Яндекс.Музыки</h1>
            
                <motion.div 
                    variants={arrowVariants}
                >
                    ↓
                </motion.div>
            </motion.a>
        </div>
    )
}
