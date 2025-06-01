import { useTranslation } from 'next-i18next';
import { serverSideTranslations } from 'next-i18next/serverSideTranslations';
import Head from 'next/head';
import Header from '../components/Header';
import Footer from '../components/Footer';

export default function About() {
  const { t } = useTranslation('common');

  return (
    <div>
      <Head>
        <title>{t('about.title')}</title>
        <meta name="description" content={t('about.description')} />
      </Head>

      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-3xl mx-auto">
          <h1 className="text-4xl font-bold mb-6">{t('about.title')}</h1>
          
          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">{t('about.introduction.title')}</h2>
            <p className="text-gray-700 mb-4">{t('about.introduction.content')}</p>
          </section>

          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">{t('about.story.title')}</h2>
            <p className="text-gray-700 mb-4">{t('about.story.content')}</p>
          </section>

          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">{t('about.vision.title')}</h2>
            <p className="text-gray-700 mb-4">{t('about.vision.content')}</p>
          </section>

          <section className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">{t('about.expertise.title')}</h2>
            <p className="text-gray-700 mb-4">{t('about.expertise.content')}</p>
          </section>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export async function getStaticProps({ locale }) {
  return {
    props: {
      ...(await serverSideTranslations(locale, ['common'])),
    },
  };
} 