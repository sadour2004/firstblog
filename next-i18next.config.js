module.exports = {
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ar', 'fr'],
  },
  localePath: './public/locales',
  reloadOnPrerender: process.env.NODE_ENV === 'development',
}; 