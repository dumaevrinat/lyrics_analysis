import { FC, ReactNode } from 'react'
import styles from './section.module.css'


type SectionProps = {
    title: string,
    children: ReactNode
}

export const Section: FC<SectionProps> = ({ title, children }) => {
    return (
        <section
            className={styles.section}
        >
            <h2>
                {title}
            </h2>

            {children}
        </section>
    )
}
