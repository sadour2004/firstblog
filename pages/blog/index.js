import { useState } from 'react';
import { useTranslation } from 'next-i18next';
import { serverSideTranslations } from 'next-i18next/serverSideTranslations';
import Head from 'next/head';
import Image from 'next/image';
import Link from 'next/link';
import Header from '../../components/Header';
import Footer from '../../components/Footer';
import BlogCard from '../../components/BlogCard';
import CategorySection from '../../components/CategorySection';
import NewsletterCTA from '../../components/NewsletterCTA';

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

export default function Blog({ posts, categories, featuredCategories }) {
  const { t } = useTranslation('common');
  const [sortBy, setSortBy] = useState('newest');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [searchQuery, setSearchQuery] = useState('');

  // Separate featured posts
  const featuredPosts = posts.filter(post => post.featured);
  const regularPosts = posts.filter(post => !post.featured);

  const filteredPosts = regularPosts
    .filter(post => {
      if (selectedCategory && post.category !== selectedCategory) return false;
      if (searchQuery) {
        const query = searchQuery.toLowerCase();
        return (
          post.title.toLowerCase().includes(query) ||
          post.excerpt.toLowerCase().includes(query)
        );
      }
      return true;
    })
    .sort((a, b) => {
      if (sortBy === 'newest') return new Date(b.date) - new Date(a.date);
      if (sortBy === 'oldest') return new Date(a.date) - new Date(b.date);
      if (sortBy === 'popular') return b.views - a.views;
      return 0;
    });

  return (
    <div>
      <Head>
        <title>{t('blog.title')}</title>
        <meta name="description" content={t('blog.description')} />
      </Head>

      <Header />

      <main>
        {/* Hero Section - Reduced height */}
        <div className="relative h-[300px] bg-gray-900">
          <Image
            src="/images/MARAKECH.jpg"
            alt="Moroccan Tourism Blog"
            layout="fill"
            objectFit="cover"
            className="opacity-50"
            priority
          />
          <div className="absolute inset-0 flex items-center justify-center text-center">
            <div className="max-w-2xl px-4">
              <h1 className="text-3xl md:text-4xl font-bold text-white mb-3">
                {t('blog.title')}
              </h1>
              <p className="text-lg text-gray-200">
                {t('blog.description')}
              </p>
            </div>
          </div>
        </div>

        <div className="container mx-auto px-4 py-8">
          <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">
            {/* Sidebar */}
            <div className="lg:col-span-1 space-y-6">
              <CategorySection
                categories={categories}
                featuredCategories={featuredCategories}
              />
              
              <NewsletterCTA />
            </div>

            {/* Main Content */}
            <div className="lg:col-span-3">
              {/* Search and Sort - More compact */}
              <div className="bg-white rounded-lg shadow-md p-3 mb-6">
                <div className="flex flex-col sm:flex-row gap-3">
                  <div className="flex-1">
                    <input
                      type="text"
                      placeholder={t('blog.searchPlaceholder')}
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      className="w-full px-3 py-2 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
                    />
                  </div>
                  <div className="flex gap-3">
                    <select
                      value={sortBy}
                      onChange={(e) => setSortBy(e.target.value)}
                      className="px-3 py-2 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
                    >
                      <option value="newest">{t('blog.sort.newest')}</option>
                      <option value="oldest">{t('blog.sort.oldest')}</option>
                      <option value="popular">{t('blog.sort.popular')}</option>
                    </select>
                    <select
                      value={selectedCategory}
                      onChange={(e) => setSelectedCategory(e.target.value)}
                      className="px-3 py-2 text-sm border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
                    >
                      <option value="">{t('blog.allCategories')}</option>
                      {categories.map((category) => (
                        <option key={category.slug} value={category.slug}>
                          {category.name}
                        </option>
                      ))}
                    </select>
                  </div>
                </div>
              </div>

              {/* Featured Posts - Reduced height */}
              {featuredPosts.length > 0 && (
                <div className="mb-8">
                  <h2 className="text-xl font-bold mb-4">{t('blog.featured')}</h2>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    {featuredPosts.map((post) => (
                      <div key={post.slug} className="relative h-[280px] rounded-lg overflow-hidden group">
                        <Image
                          src={post.image}
                          alt={post.title}
                          layout="fill"
                          objectFit="cover"
                          className="transition-transform duration-300 group-hover:scale-105"
                        />
                        <div className="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent">
                          <div className="absolute bottom-0 p-4">
                            {post.category && (
                              <span className="inline-block bg-blue-600 text-white px-2 py-1 rounded-full text-xs mb-2">
                                {post.category}
                              </span>
                            )}
                            <h3 className="text-lg font-bold text-white mb-2">
                              {post.title}
                            </h3>
                            <p className="text-sm text-gray-200 mb-3 line-clamp-2">
                              {post.excerpt}
                            </p>
                            <Link
                              href={`/blog/${post.slug}`}
                              className="inline-flex items-center text-sm text-white hover:text-blue-400 transition-colors"
                            >
                              {t('blog.readMore')} →
                            </Link>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Regular Posts */}
              <div>
                <h2 className="text-xl font-bold mb-4">{t('blog.latest')}</h2>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {filteredPosts.map((post) => (
                    <BlogCard key={post.slug} post={post} />
                  ))}
                </div>
              </div>

              {/* Pagination - More compact */}
              {filteredPosts.length > 0 && (
                <div className="mt-8 flex justify-center">
                  <nav className="flex items-center space-x-1">
                    <button className="px-2 py-1 text-sm rounded-lg border border-gray-300 hover:bg-gray-50 disabled:opacity-50">
                      {t('blog.pagination.previous')}
                    </button>
                    <button className="px-2 py-1 text-sm rounded-lg bg-blue-600 text-white hover:bg-blue-700">
                      1
                    </button>
                    <button className="px-2 py-1 text-sm rounded-lg border border-gray-300 hover:bg-gray-50">
                      2
                    </button>
                    <button className="px-2 py-1 text-sm rounded-lg border border-gray-300 hover:bg-gray-50">
                      3
                    </button>
                    <button className="px-2 py-1 text-sm rounded-lg border border-gray-300 hover:bg-gray-50">
                      {t('blog.pagination.next')}
                    </button>
                  </nav>
                </div>
              )}

              {/* No Results */}
              {filteredPosts.length === 0 && (
                <div className="text-center py-8">
                  <h3 className="text-lg font-semibold text-gray-900 mb-2">
                    {t('blog.noResults.title')}
                  </h3>
                  <p className="text-sm text-gray-600">
                    {t('blog.noResults.description')}
                  </p>
                </div>
              )}
            </div>
          </div>
        </div>
      </main>

      <Footer />
    </div>
  );
}

export async function getStaticProps({ locale }) {
  // This would typically fetch from your API or CMS
  const posts = [
    {
      slug: 'discovering-marrakech',
      title: 'Discovering the Magic of Marrakech',
      excerpt: 'Explore the vibrant streets, historic medina, and hidden gems of Morocco\'s most famous city.',
      date: '2024-03-15',
      category: 'destinations',
      image: '/images/MARAKECH.jpg',
      author: {
        name: 'Sarah Johnson',
        avatar: '/images/author1.jpg'
      },
      views: 1234,
      featured: true
    },
    {
      slug: 'exploring-tangier',
      title: 'Exploring Tangier: Gateway to Africa',
      excerpt: 'Discover the unique blend of Mediterranean and Moroccan cultures in Tangier...',
      date: '2024-03-10',
      category: 'destinations',
      image: '/images/TANGER.jpg',
      author: {
        name: 'Mohammed Alami',
        avatar: '/images/author2.jpg'
      },
      views: 856,
      featured: true
    },
    // Add more sample posts here
  ];

  const categories = [
    { slug: 'destinations', name: 'Destinations', postCount: 12 },
    { slug: 'travel-tips', name: 'Travel Tips', postCount: 8 },
    { slug: 'moroccan-culture', name: 'Moroccan Culture', postCount: 15 },
    { slug: 'food', name: 'Food & Cuisine', postCount: 6 },
    { slug: 'history', name: 'History & Heritage', postCount: 9 }
  ];

  const featuredCategories = [
    { slug: 'destinations', name: 'Top Destinations', postCount: 12 },
    { slug: 'moroccan-culture', name: 'Cultural Insights', postCount: 15 }
  ];

  return {
    props: {
      ...(await serverSideTranslations(locale, ['common'])),
      posts,
      categories,
      featuredCategories
    }
  };
} 