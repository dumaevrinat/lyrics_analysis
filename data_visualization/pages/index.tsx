import type { NextPage } from 'next'
import Head from 'next/head'
import { Epochs } from 'components/sections/home/epochs'
import { Intro } from 'components/sections/home/intro'
import { TypicalWordsGenres } from 'components/sections/home/typical-words-genres'
import { UniqueWordsGenres } from 'components/sections/home/unique-words-genres'
import styles from 'styles/home.module.css'
import { UniqueWordsArtists } from 'components/sections/home/unique-words-artists'
import { UniqueWordsPoses } from 'components/sections/home/unique-words-poses'
import { TypicalWordsPoses } from 'components/sections/home/typical-words-poses'
import { Section } from 'components/section'


const Home: NextPage = () => {
    return (
        <>
            <Head>
                <title>Анализ данных Яндекс.Музыки</title>
                <meta name='description' content='Анализ данных Яндекс.Музыки' />
                <meta name='viewport' content='width=device-width, initial-scale=1' />
                <meta name='theme-color' content='#000' />
            </Head>

            <main className={styles.main}>
                <Intro />
                
                <div id='start'>
                    <UniqueWordsGenres />
                </div>
                
                <UniqueWordsArtists />
                <UniqueWordsPoses />

                <TypicalWordsGenres />
                <TypicalWordsPoses />

                <Epochs/>
            </main>

            <footer className={styles.footer}>
                <Section title={''} className={styles.footerSection}>
                    <a 
                        className='link' 
                        href='https://github.com/dumaevrinat/lyrics_analysis' 
                        target='_blank'
                    >
                        GitHub репозиторий
                    </a>
                    <a 
                        className='link' 
                        href='https://github.com/dumaevrinat' 
                        target='_blank'
                    >
                        Думаев Ринат
                    </a>
                </Section>
            </footer>
        </>
    )
}

export default Home
