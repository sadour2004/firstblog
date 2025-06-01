import { useTranslation } from 'next-i18next';
import { serverSideTranslations } from 'next-i18next/serverSideTranslations';
import Head from 'next/head';
import Link from 'next/link';
import Image from 'next/image';
import { useEffect, useState } from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

// Hero images for carousel
const heroImages = [
  {
    src: '/images/MARAKECH.jpg',
    alt: 'Marrakech - The Red City'
  },
  {
    src: '/images/CASABLANCA.jpg',
    alt: 'Casablanca - Modern Morocco'
  },
  {
    src: '/images/FEZ.jpg',
    alt: 'Fez - Cultural Capital'
  },
  {
    src: '/images/RABAT.jpg',
    alt: 'Rabat - The Capital'
  },
  {
    src: '/images/TANGER.jpg',
    alt: 'Tangier - Gateway to Africa'
  }
];

// Mock data for featured destinations
const featuredDestinations = [
  {
    id: 1,
    name: 'Tangier',
    image: '/images/TANGER.jpg',
    description: 'Where the Mediterranean meets the Atlantic',
    slug: 'tangier'
  },
  {
    id: 2,
    name: 'Rabat',
    image: '/images/RABAT.jpg',
    description: 'The modern capital with ancient roots',
    slug: 'rabat'
  },
  {
    id: 3,
    name: 'Marrakech',
    image: '/images/MARAKECH.jpg',
    description: 'The red city of Morocco',
    slug: 'marrakech'
  },
  {
    id: 4,
    name: 'Casablanca',
    image: '/images/CASABLANCA.jpg',
    description: 'Morocco\'s economic heart',
    slug: 'casablanca'
  },
  {
    id: 5,
    name: 'Fez',
    image: '/images/FEZ.jpg',
    description: 'The cultural and spiritual capital',
    slug: 'fez'
  }
];

// Mock data for featured posts
const featuredPosts = [
  {
    id: 1,
    title: 'Top 10 Hidden Gems in Marrakech',
    excerpt: 'Discover the secret spots that most tourists miss...',
    image: '/images/MARAKECH.jpg',
    slug: 'hidden-gems-marrakech'
  },
  {
    id: 2,
    title: 'A Guide to Tangier\'s Beaches',
    excerpt: 'From pristine shores to vibrant beach clubs...',
    image: '/images/TANGER.jpg',
    slug: 'tangier-beaches'
  }
];

export default function Home() {
  const { t } = useTranslation('common');
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentImageIndex((prevIndex) => (prevIndex + 1) % heroImages.length);
    }, 3000); // 3 seconds

    return () => clearInterval(timer);
  }, []);

  return (
    <div className="min-h-screen bg-gray-50">
      <Head>
        <title>{t('home.title')}</title>
        <meta name="description" content={t('home.description')} />
      </Head>

      <Header />
      
      {/* Hero Section with Carousel */}
      <section className="relative h-[600px] flex items-center justify-center overflow-hidden">
        {heroImages.map((image, index) => (
          <div
            key={image.src}
            className={`absolute inset-0 transition-opacity duration-1000 ${
              index === currentImageIndex ? 'opacity-100' : 'opacity-0'
            }`}
          >
            <Image
              src={image.src}
              alt={image.alt}
              layout="fill"
              objectFit="cover"
              priority={index === 0}
            />
            <div className="absolute inset-0 bg-black bg-opacity-50"></div>
          </div>
        ))}
        <div className="relative z-10 text-center text-white px-4">
          <h1 className="text-5xl md:text-6xl font-bold mb-6 animate-fade-in">
            {t('home.hero.title')}
          </h1>
          <p className="text-xl md:text-2xl mb-8 max-w-3xl mx-auto">
            {t('home.hero.subtitle')}
          </p>
          <Link href="/blog" className="inline-block bg-blue-600 text-white px-8 py-3 rounded-full text-lg font-semibold hover:bg-blue-700 transition-colors">
            {t('home.hero.cta')}
          </Link>
        </div>

        {/* Carousel Indicators */}
        <div className="absolute bottom-8 left-0 right-0 flex justify-center space-x-2">
          {heroImages.map((_, index) => (
            <button
              key={index}
              className={`w-3 h-3 rounded-full transition-colors ${
                index === currentImageIndex ? 'bg-white' : 'bg-white/50'
              }`}
              onClick={() => setCurrentImageIndex(index)}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      </section>

      {/* Featured Destinations */}
      <section className="py-16 px-4">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">{t('home.destinations.title')}</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {featuredDestinations.map((destination) => (
              <div key={destination.id} className="bg-white rounded-lg shadow-lg overflow-hidden transform hover:scale-105 transition-transform">
                <div className="relative h-48">
                  <Image
                    src={destination.image}
                    alt={destination.name}
                    layout="fill"
                    objectFit="cover"
                  />
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-semibold mb-2">{destination.name}</h3>
                  <p className="text-gray-600 mb-4">{destination.description}</p>
                  <Link href={`/blog/${destination.slug}`} className="text-blue-600 hover:text-blue-800 font-medium">
                    {t('home.destinations.explore')} →
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Posts */}
      <section className="py-16 px-4 bg-gray-100">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-12">{t('home.featured.title')}</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {featuredPosts.map((post) => (
              <article key={post.id} className="bg-white rounded-lg shadow-lg overflow-hidden">
                <div className="relative h-64">
                  <Image
                    src={post.image}
                    alt={post.title}
                    layout="fill"
                    objectFit="cover"
                  />
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-semibold mb-2">{post.title}</h3>
                  <p className="text-gray-600 mb-4">{post.excerpt}</p>
                  <Link href={`/blog/${post.slug}`} className="text-blue-600 hover:text-blue-800 font-medium">
                    {t('home.featured.readMore')} →
                  </Link>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* Newsletter Section */}
      <section className="py-16 px-4 bg-blue-600 text-white">
        <div className="max-w-4xl mx-auto text-center">
          <h2 className="text-3xl font-bold mb-4">{t('home.newsletter.title')}</h2>
          <p className="text-xl mb-8">{t('home.newsletter.description')}</p>
          <form className="flex flex-col md:flex-row gap-4 max-w-2xl mx-auto">
            <input
              type="email"
              placeholder={t('home.newsletter.placeholder')}
              className="flex-1 px-6 py-3 rounded-full text-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-300"
            />
            <button
              type="submit"
              className="bg-white text-blue-600 px-8 py-3 rounded-full font-semibold hover:bg-gray-100 transition-colors"
            >
              {t('home.newsletter.subscribe')}
            </button>
          </form>
        </div>
      </section>

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