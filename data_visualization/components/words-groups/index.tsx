import { FC, Fragment } from 'react'
import styles from './words-groups.module.css'
import { WordsGroup } from './words-group'


export type WordsGroup = {
    label: string,
    words: string[]
}

export type WordsGroupsProps = {
    groups: WordsGroup[]
}

export const WordsGroups: FC<WordsGroupsProps> = ({ groups }) => {
    return (
        <div className={styles.wordsGroups}>
            {groups.map(group =>
                <Fragment key={group.label}>
                    <span
                        className={styles.label}
                    >
                        {group.label}
                    </span>

                    <WordsGroup
                        className={styles.group}
                        words={group.words}
                    />
                </Fragment>
            )}
        </div>
    )
}
