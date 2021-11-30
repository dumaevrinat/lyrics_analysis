import clsx from 'clsx'
import { FC, ReactNode } from 'react'
import styles from './section.module.css'


type SectionProps = {
    title: string,
    className?: string,
    children: ReactNode
}

export const Section: FC<SectionProps> = ({ title, className, children }) => {
    return (
        <section
            className={clsx(styles.section, className && className)}
        >
            {title &&
                <h2>
                    {title}
                </h2>
            }

            {children}
        </section>
    )
}
