import { FC, ReactElement } from 'react'
import { RadioProps } from 'components/radio'
import styles from './radio-group.module.css'


export type RadioGroupProps = {
    children: ReactElement<RadioProps> | ReactElement<RadioProps>[],
}

export const RadioGroup: FC<RadioGroupProps> = ({ children }) => {
    return (
        <div className={styles.radioGroup}>
            {children}
        </div>
    )
}