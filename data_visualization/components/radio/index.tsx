import { DetailedHTMLProps, FC, InputHTMLAttributes, ReactNode } from 'react'
import clsx from 'clsx'
import styles from './radio.module.css'


export type RadioProps = DetailedHTMLProps<InputHTMLAttributes<HTMLInputElement>, HTMLInputElement> & {
    children?: ReactNode | string
}

export const Radio: FC<RadioProps> = ({ className, id, children, value, ...rest }) => {
    return (
        <>
            <input
                id={id}
                type='radio'
                value={value}
                className={styles.radio}
                {...rest}
            />
            <label
                htmlFor={id}
                className={clsx(styles.label, className)}
            >
                {children ? children : value}
            </label>
        </>
    )
}
