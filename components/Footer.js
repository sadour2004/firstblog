import Link from 'next/link';
import { useTranslation } from 'next-i18next';

export default function Footer() {
  const { t } = useTranslation('common');

  return (
    <footer className="bg-gray-800 text-white py-8">
      <div className="container mx-auto px-4">
        <div className="flex flex-wrap justify-between">
          <div className="w-full md:w-1/3 mb-4">
            <h3 className="text-lg font-bold mb-2">{t('footer.importantLinks')}</h3>
            <ul>
              <li>
                <Link href="/privacy" className="hover:underline">
                  {t('footer.privacy')}
                </Link>
              </li>
              <li>
                <Link href="/terms" className="hover:underline">
                  {t('footer.terms')}
                </Link>
              </li>
            </ul>
          </div>
          <div className="w-full md:w-1/3 mb-4">
            <h3 className="text-lg font-bold mb-2">{t('footer.socialMedia')}</h3>
            <div className="flex space-x-4">
              <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" className="hover:underline">Facebook</a>
              <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" className="hover:underline">Instagram</a>
              <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" className="hover:underline">Twitter</a>
            </div>
          </div>
          <div className="w-full md:w-1/3 mb-4">
            <h3 className="text-lg font-bold mb-2">{t('footer.newsletter')}</h3>
            <form className="flex">
              <input type="email" placeholder={t('footer.emailPlaceholder')} className="px-4 py-2 w-full rounded-l" />
              <button type="submit" className="bg-blue-500 px-4 py-2 rounded-r">{t('footer.subscribe')}</button>
            </form>
          </div>
        </div>
        <div className="text-center mt-4">
          <p>{t('footer.copyright')}</p>
        </div>
      </div>
    </footer>
  );
} 