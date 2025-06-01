import { useTranslation } from 'next-i18next';
import { serverSideTranslations } from 'next-i18next/serverSideTranslations';
import Head from 'next/head';
import Link from 'next/link';
import Header from '../../components/Header';
import Footer from '../../components/Footer';

// Mock blog posts data - In a real application, this would come from an API or CMS
const blogPosts = [
  {
    id: 1,
    slug: 'exploring-tangier',
    title: 'Exploring Tangier: Gateway to Africa',
    excerpt: 'Discover the unique blend of Mediterranean and Moroccan cultures in Tangier...',
    category: 'Tangier',
    date: '2024-03-15',
    image: '/images/TANGER.jpg'
  },
  {
    id: 2,
    slug: 'rabat-capital-charm',
    title: 'Rabat: The Capital\'s Hidden Charm',
    excerpt: 'Experience the perfect balance of history and modernity in Morocco\'s capital...',
    category: 'Rabat',
    date: '2024-03-10',
    image: '/images/RABAT.jpg'
  },
  {
    id: 3,
    slug: 'marrakech-red-city',
    title: 'Marrakech: The Red City of Morocco',
    excerpt: 'Immerse yourself in the vibrant culture and history of Marrakech...',
    category: 'Marrakech',
    date: '2024-03-05',
    image: '/images/MARAKECH.jpg'
  },
  {
    id: 4,
    slug: 'casablanca-modern-morocco',
    title: 'Casablanca: Modern Morocco\'s Heart',
    excerpt: 'Discover the modern side of Morocco in its largest city...',
    category: 'Casablanca',
    date: '2024-03-01',
    image: '/images/CASABLANCA.jpg'
  },
  {
    id: 5,
    slug: 'fez-cultural-capital',
    title: 'Fez: Morocco\'s Cultural Capital',
    excerpt: 'Step back in time in the world\'s largest car-free urban area...',
    category: 'Fez',
    date: '2024-02-25',
    image: '/images/FEZ.jpg'
  }
];

// Format date consistently
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  });
};

export default function Blog() {
  const { t } = useTranslation('common');

  return (
    <div>
      <Head>
        <title>{t('blog.title')}</title>
        <meta name="description" content={t('blog.description')} />
      </Head>

      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-4xl font-bold mb-8">{t('blog.title')}</h1>

          {/* Categories */}
          <div className="mb-8">
            <h2 className="text-2xl font-semibold mb-4">{t('blog.categories')}</h2>
            <div className="flex flex-wrap gap-2">
              {['Tangier', 'Rabat', 'Marrakech', 'Casablanca', 'Fez', 'Moroccan Culture', 'Travel Tips'].map((category) => (
                <Link
                  key={category}
                  href={`/blog/category/${category.toLowerCase()}`}
                  className="bg-gray-200 hover:bg-gray-300 px-4 py-2 rounded-full text-sm"
                >
                  {category}
                </Link>
              ))}
            </div>
          </div>

          {/* Blog Posts Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {blogPosts.map((post) => (
              <article key={post.id} className="bg-white rounded-lg shadow-md overflow-hidden">
                <div className="aspect-w-16 aspect-h-9">
                  <img
                    src={post.image}
                    alt={post.title}
                    className="object-cover w-full h-48"
                  />
                </div>
                <div className="p-6">
                  <div className="text-sm text-gray-500 mb-2">
                    {post.category} • {formatDate(post.date)}
                  </div>
                  <h2 className="text-xl font-semibold mb-2">
                    <Link href={`/blog/${post.slug}`} className="hover:text-blue-600">
                      {post.title}
                    </Link>
                  </h2>
                  <p className="text-gray-600 mb-4">{post.excerpt}</p>
                  <Link
                    href={`/blog/${post.slug}`}
                    className="text-blue-600 hover:text-blue-800 font-medium"
                  >
                    {t('blog.readMore')} →
                  </Link>
                </div>
              </article>
            ))}
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