import Link from 'next/link';
import { useTranslation } from 'next-i18next';

const categoryIcons = {
  'travel-tips': (
    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7" />
    </svg>
  ),
  'moroccan-culture': (
    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
    </svg>
  ),
  'food': (
    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
    </svg>
  ),
  'destinations': (
    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
    </svg>
  ),
  'history': (
    <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
  ),
};

export default function CategorySection({ categories, featuredCategories }) {
  const { t } = useTranslation('common');

  return (
    <div className="bg-white rounded-xl shadow-lg overflow-hidden">
      {/* Featured Categories */}
      {featuredCategories && featuredCategories.length > 0 && (
        <div className="p-6 bg-gradient-to-br from-blue-600 to-blue-800 text-white">
          <h3 className="text-xl font-bold mb-4">{t('blog.featuredCategories')}</h3>
          <div className="space-y-4">
            {featuredCategories.map((category) => (
              <Link
                key={category.slug}
                href={`/blog/category/${category.slug}`}
                className="flex items-center p-4 bg-white/10 rounded-lg hover:bg-white/20 transition-colors group"
              >
                <div className="w-12 h-12 bg-white/20 rounded-lg flex items-center justify-center mr-4 group-hover:bg-white/30 transition-colors">
                  {categoryIcons[category.slug] || categoryIcons['destinations']}
                </div>
                <div>
                  <h4 className="font-semibold text-lg">{category.name}</h4>
                  <p className="text-blue-100 text-sm">{category.postCount} {t('blog.posts')}</p>
                </div>
              </Link>
            ))}
          </div>
        </div>
      )}
      
      {/* All Categories */}
      <div className="p-6">
        <h3 className="text-xl font-bold mb-4 text-gray-900">{t('blog.categories')}</h3>
        <div className="space-y-3">
          {categories.map((category) => (
            <Link
              key={category.slug}
              href={`/blog/category/${category.slug}`}
              className="flex items-center p-3 rounded-lg hover:bg-gray-50 transition-colors group"
            >
              <div className="w-10 h-10 bg-blue-50 rounded-lg flex items-center justify-center mr-3 text-blue-600 group-hover:bg-blue-100 transition-colors">
                {categoryIcons[category.slug] || categoryIcons['destinations']}
              </div>
              <span className="text-gray-700 font-medium group-hover:text-blue-600 transition-colors">
                {category.name}
              </span>
              <span className="ml-auto text-sm text-gray-500 bg-gray-100 px-2 py-1 rounded-full">
                {category.postCount}
              </span>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
} 