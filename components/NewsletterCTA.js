import { useState } from 'react';
import { useTranslation } from 'next-i18next';

export default function NewsletterCTA() {
  const { t } = useTranslation('common');
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState('idle');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus('loading');
    
    // Here you would typically make an API call to your newsletter service
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000));
      setStatus('success');
      setEmail('');
    } catch (error) {
      setStatus('error');
    }
  };

  return (
    <div className="relative overflow-hidden rounded-xl bg-gradient-to-br from-blue-600 via-blue-700 to-blue-800 p-8">
      {/* Decorative elements */}
      <div className="absolute -top-12 -right-12 w-24 h-24 bg-white/10 rounded-full blur-2xl"></div>
      <div className="absolute -bottom-12 -left-12 w-24 h-24 bg-white/10 rounded-full blur-2xl"></div>
      
      <div className="relative">
        <div className="text-center mb-8">
          <h2 className="text-2xl font-bold text-white mb-3">
            {t('blog.newsletter.title')}
          </h2>
          <p className="text-blue-100">
            {t('blog.newsletter.description')}
          </p>
        </div>
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="relative">
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder={t('blog.newsletter.placeholder')}
              className="w-full px-4 py-3 rounded-lg bg-white/10 border border-white/20 text-white placeholder-blue-200 focus:outline-none focus:ring-2 focus:ring-white/50 transition-all"
              required
            />
            <div className="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none">
              <svg className="w-5 h-5 text-blue-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
          </div>
          
          <button
            type="submit"
            disabled={status === 'loading'}
            className="w-full bg-white text-blue-600 px-6 py-3 rounded-lg font-semibold hover:bg-blue-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {status === 'loading' ? (
              <span className="flex items-center justify-center">
                <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                {t('blog.newsletter.subscribing')}
              </span>
            ) : (
              t('blog.newsletter.subscribe')
            )}
          </button>
        </form>
        
        {status === 'success' && (
          <div className="mt-4 p-3 bg-green-500/20 rounded-lg text-green-100 text-center">
            {t('blog.newsletter.success')}
          </div>
        )}
        
        {status === 'error' && (
          <div className="mt-4 p-3 bg-red-500/20 rounded-lg text-red-100 text-center">
            {t('blog.newsletter.error')}
          </div>
        )}
      </div>
    </div>
  );
} 