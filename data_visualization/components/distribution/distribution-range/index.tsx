import { AnimatePresence, motion, Variants } from 'framer-motion'
import { FC } from 'react'
import styles from './distribution-range.module.css'


export type RangeItem = {
    value: number,
    label: string
}

export type DistributionRangeProps = {
    min: number,
    max: number,
    items: RangeItem[]
}

const rangeItemVariants: Variants = {
    initial: {
        opacity: 0,
        scale: 0
    },
    animate: index => ({
        opacity: 1,
        scale: 1,
        transition: {
            delay: index * 0.01,
            bounce: 0
        }
    }),
    exit: {
        opacity: 0,
        scale: 0
    }
}

export const DistributionRange: FC<DistributionRangeProps> = ({ min, max, items }) => {
    return (
        <>
            <span className={styles.rangeLabel}>
                {`${Math.floor(min)}—${Math.floor(max)}`}
            </span>

            <div className={styles.rangeItems}>
                {items.map((item, index) =>
                    <AnimatePresence key={item.label}>
                        <motion.div
                            className={styles.rangeItem}
                            variants={rangeItemVariants}
                            custom={index}
                            initial='initial'
                            animate='animate'
                            exit='exit'
                        >
                            <span className={styles.rangeItemLabel}>
                                {item.label}
                            </span>
                            <span className={styles.rangeItemValue}>
                                {Math.floor(item.value)}
                            </span>
                        </motion.div>
                    </AnimatePresence>
                )}
            </div>
        </>
    )
}
