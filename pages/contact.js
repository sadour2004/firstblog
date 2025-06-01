import { useTranslation } from 'next-i18next';
import { serverSideTranslations } from 'next-i18next/serverSideTranslations';
import Head from 'next/head';
import Header from '../components/Header';
import Footer from '../components/Footer';

export default function Contact() {
  const { t } = useTranslation('common');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission here
    console.log('Form submitted');
  };

  return (
    <div>
      <Head>
        <title>{t('contact.title')}</title>
        <meta name="description" content={t('contact.description')} />
      </Head>

      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          <h1 className="text-4xl font-bold mb-8">{t('contact.title')}</h1>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {/* Contact Form */}
            <div className="bg-white p-6 rounded-lg shadow-md">
              <h2 className="text-2xl font-semibold mb-4">{t('contact.form.title')}</h2>
              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">
                    {t('contact.form.name')}
                  </label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                  />
                </div>
                <div>
                  <label htmlFor="email" className="block text-sm font-medium text-gray-700 mb-1">
                    {t('contact.form.email')}
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                  />
                </div>
                <div>
                  <label htmlFor="message" className="block text-sm font-medium text-gray-700 mb-1">
                    {t('contact.form.message')}
                  </label>
                  <textarea
                    id="message"
                    name="message"
                    rows="4"
                    required
                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500"
                  ></textarea>
                </div>
                <button
                  type="submit"
                  className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors"
                >
                  {t('contact.form.submit')}
                </button>
              </form>
            </div>

            {/* Contact Information */}
            <div className="bg-white p-6 rounded-lg shadow-md">
              <h2 className="text-2xl font-semibold mb-4">{t('contact.info.title')}</h2>
              <div className="space-y-4">
                <div>
                  <h3 className="text-lg font-medium mb-2">{t('contact.info.email')}</h3>
                  <p className="text-gray-600">contact@moroccantourism.com</p>
                </div>
                <div>
                  <h3 className="text-lg font-medium mb-2">{t('contact.info.phone')}</h3>
                  <p className="text-gray-600">+212 5XX-XXXXXX</p>
                </div>
                <div>
                  <h3 className="text-lg font-medium mb-2">{t('contact.info.social')}</h3>
                  <div className="flex space-x-4">
                    <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:text-blue-800">
                      Facebook
                    </a>
                    <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:text-blue-800">
                      Instagram
                    </a>
                    <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:text-blue-800">
                      Twitter
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
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