import Image from 'next/image';
import Link from 'next/link';
import { useTranslation } from 'next-i18next';

export default function BlogCard({ post }) {
  const { t, i18n } = useTranslation('common');
  
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleDateString(i18n.language, {
      year: 'numeric',
      month: '2-digit',
      day: '2-digit'
    });
  };
  
  return (
    <article className="bg-white rounded-lg shadow-md overflow-hidden transition-transform duration-300 hover:shadow-lg hover:-translate-y-1">
      <div className="relative h-40 overflow-hidden group">
        <Image
          src={post.image}
          alt={post.title}
          layout="fill"
          objectFit="cover"
          className="transition-transform duration-300 group-hover:scale-105"
          priority={post.featured}
        />
        {post.category && (
          <div className="absolute top-3 left-3 bg-blue-600 text-white px-2 py-1 rounded-full text-xs">
            {post.category}
          </div>
        )}
      </div>
      
      <div className="p-4">
        <div className="flex items-center text-xs text-gray-500 mb-2">
          <svg className="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
          {formatDate(post.date)}
        </div>
        
        <h2 className="text-lg font-semibold mb-2 transition-colors duration-300 group-hover:text-blue-600 line-clamp-2">
          {post.title}
        </h2>
        
        <p className="text-sm text-gray-600 mb-3 line-clamp-2">
          {post.excerpt}
        </p>
        
        <div className="flex items-center justify-between">
          <Link href={`/blog/${post.slug}`} className="text-sm text-blue-600 font-medium hover:text-blue-700 transition-colors">
            {t('blog.readMore')} →
          </Link>
          
          {post.author && (
            <div className="flex items-center">
              <div className="w-6 h-6 rounded-full overflow-hidden mr-2">
                <Image
                  src={post.author.avatar}
                  alt={post.author.name}
                  width={24}
                  height={24}
                  className="object-cover"
                />
              </div>
              <span className="text-xs text-gray-600">{post.author.name}</span>
            </div>
          )}
        </div>
      </div>
    </article>
  );
} 