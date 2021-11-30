import { FC } from 'react'
import styles from './intro.module.css'


export const Intro: FC = () => {
    return (
        <div className={styles.intro}>
            <h1>Анализ данных<br/>Яндекс.Музыки</h1>
        </div>
    )
}
