import { useTranslation } from 'next-i18next';
import Link from 'next/link';
import Image from 'next/image';
import { useState, useEffect } from 'react';

export default function Header() {
  const { t } = useTranslation('common');
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 20);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header className={`fixed w-full z-50 transition-all duration-300 ${
      isScrolled ? 'bg-white shadow-md' : 'bg-transparent'
    }`}>
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-24 md:h-28">
          {/* Logo */}
          <Link href="/" className="flex items-center">
            <div className="relative w-20 h-20 md:w-28 md:h-28">
              <Image
                src="/images/TRAVEL.png"
                alt="Travel Logo"
                layout="fill"
                objectFit="contain"
                priority
              />
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center space-x-8">
            <Link href="/" className={`font-medium hover:text-blue-600 transition-colors ${
              isScrolled ? 'text-gray-700' : 'text-white'
            }`}>
              {t('nav.home')}
            </Link>
            <Link href="/about" className={`font-medium hover:text-blue-600 transition-colors ${
              isScrolled ? 'text-gray-700' : 'text-white'
            }`}>
              {t('nav.about')}
            </Link>
            <Link href="/blog" className={`font-medium hover:text-blue-600 transition-colors ${
              isScrolled ? 'text-gray-700' : 'text-white'
            }`}>
              {t('nav.blog')}
            </Link>
            <Link href="/contact" className={`font-medium hover:text-blue-600 transition-colors ${
              isScrolled ? 'text-gray-700' : 'text-white'
            }`}>
              {t('nav.contact')}
            </Link>
            <div className="flex items-center space-x-4 ml-4">
              <Link href="/" locale="en" className={`font-medium hover:text-blue-600 transition-colors ${
                isScrolled ? 'text-gray-700' : 'text-white'
              }`}>
                EN
              </Link>
              <Link href="/" locale="fr" className={`font-medium hover:text-blue-600 transition-colors ${
                isScrolled ? 'text-gray-700' : 'text-white'
              }`}>
                FR
              </Link>
              <Link href="/" locale="ar" className={`font-medium hover:text-blue-600 transition-colors ${
                isScrolled ? 'text-gray-700' : 'text-white'
              }`}>
                عربي
              </Link>
            </div>
          </nav>

          {/* Tablet Navigation (hidden on mobile and desktop) */}
          <nav className="hidden md:flex lg:hidden items-center space-x-6">
            <Link href="/" className={`font-medium hover:text-blue-600 transition-colors ${
              isScrolled ? 'text-gray-700' : 'text-white'
            }`}>
              {t('nav.home')}
            </Link>
            <Link href="/blog" className={`font-medium hover:text-blue-600 transition-colors ${
              isScrolled ? 'text-gray-700' : 'text-white'
            }`}>
              {t('nav.blog')}
            </Link>
            <div className="flex items-center space-x-3 ml-2">
              <Link href="/" locale="en" className={`font-medium hover:text-blue-600 transition-colors ${
                isScrolled ? 'text-gray-700' : 'text-white'
              }`}>
                EN
              </Link>
              <Link href="/" locale="fr" className={`font-medium hover:text-blue-600 transition-colors ${
                isScrolled ? 'text-gray-700' : 'text-white'
              }`}>
                FR
              </Link>
              <Link href="/" locale="ar" className={`font-medium hover:text-blue-600 transition-colors ${
                isScrolled ? 'text-gray-700' : 'text-white'
              }`}>
                عربي
              </Link>
            </div>
          </nav>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
            aria-label="Toggle menu"
          >
            <div className={`w-6 h-0.5 bg-current mb-1.5 transition-all ${
              isScrolled ? 'bg-gray-900' : 'bg-white'
            }`}></div>
            <div className={`w-6 h-0.5 bg-current mb-1.5 transition-all ${
              isScrolled ? 'bg-gray-900' : 'bg-white'
            }`}></div>
            <div className={`w-6 h-0.5 bg-current transition-all ${
              isScrolled ? 'bg-gray-900' : 'bg-white'
            }`}></div>
          </button>
        </div>

        {/* Mobile Menu */}
        <div className={`md:hidden transition-all duration-300 ease-in-out ${
          isMobileMenuOpen ? 'max-h-96 opacity-100' : 'max-h-0 opacity-0'
        } overflow-hidden bg-white shadow-lg rounded-b-lg`}>
          <nav className="py-4 px-4 space-y-4">
            <Link href="/" className="block font-medium text-gray-700 hover:text-blue-600 transition-colors">
              {t('nav.home')}
            </Link>
            <Link href="/about" className="block font-medium text-gray-700 hover:text-blue-600 transition-colors">
              {t('nav.about')}
            </Link>
            <Link href="/blog" className="block font-medium text-gray-700 hover:text-blue-600 transition-colors">
              {t('nav.blog')}
            </Link>
            <Link href="/contact" className="block font-medium text-gray-700 hover:text-blue-600 transition-colors">
              {t('nav.contact')}
            </Link>
            <div className="flex items-center space-x-4 pt-4 border-t border-gray-200">
              <Link href="/" locale="en" className="font-medium text-gray-700 hover:text-blue-600 transition-colors">
                EN
              </Link>
              <Link href="/" locale="fr" className="font-medium text-gray-700 hover:text-blue-600 transition-colors">
                FR
              </Link>
              <Link href="/" locale="ar" className="font-medium text-gray-700 hover:text-blue-600 transition-colors">
                عربي
              </Link>
            </div>
          </nav>
        </div>
      </div>
    </header>
  );
} 