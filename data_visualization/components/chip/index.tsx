import { DetailedHTMLProps, FC, HTMLAttributes } from 'react'
import clsx from 'clsx'
import styles from './chip.module.css'


type ChipProps = DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement> & {
    title: string,
    color?: string
}

export const Chip: FC<ChipProps> = ({ title, color, className, ...rest }) => {
    const style = color ? {
        borderColor: color
    } : {}

    return (
        <div
            className={clsx(styles.chip, className)}
            style={style}
            {...rest}
        >
            {title}
        </div>
    )
}
