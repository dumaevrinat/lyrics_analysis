import { motion } from 'framer-motion'
import { FC } from 'react'
import styles from './circle-counter.module.css'


type CircleCounterProps = {
    title: string,
    count: number,
    max: number
}

const BASE_HEIGHT = 250

export const CircleCounter: FC<CircleCounterProps> = ({ title, count, max }) => {
    return (
        <div className={styles.circleCounter}>
            <div
                className={styles.circle}
                style={{ 'height': `${count / max * BASE_HEIGHT}px` }}
            >
                <motion.span
                    className={styles.value}
                    whileHover={{
                        scale: 1.7,
                    }}
                >
                    {Math.floor(count)}
                </motion.span>
            </div>

            <span className={styles.title}>
                {title}
            </span>
        </div>
    )
}
