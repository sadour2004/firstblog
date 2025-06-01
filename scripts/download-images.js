const https = require('https');
const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const images = [
  {
    url: 'https://images.unsplash.com/photo-1548013146-72479768bada',
    filename: 'hero-morocco.jpg',
    width: 1920,
    height: 1080
  },
  {
    url: 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff',
    filename: 'tangier.jpg',
    width: 800,
    height: 600
  },
  {
    url: 'https://images.unsplash.com/photo-1591456983933-0c264720bcd3',
    filename: 'rabat.jpg',
    width: 800,
    height: 600
  },
  {
    url: 'https://images.unsplash.com/photo-1591456983933-0c264720bcd3',
    filename: 'marrakech.jpg',
    width: 800,
    height: 600
  },
  {
    url: 'https://images.unsplash.com/photo-1591456983933-0c264720bcd3',
    filename: 'casablanca.jpg',
    width: 800,
    height: 600
  },
  {
    url: 'https://images.unsplash.com/photo-1591456983933-0c264720bcd3',
    filename: 'fez.jpg',
    width: 800,
    height: 600
  },
  {
    url: 'https://images.unsplash.com/photo-1591456983933-0c264720bcd3',
    filename: 'marrakech-hidden.jpg',
    width: 800,
    height: 600
  },
  {
    url: 'https://images.unsplash.com/photo-1591456983933-0c264720bcd3',
    filename: 'tangier-beach.jpg',
    width: 800,
    height: 600
  }
];

const downloadImage = (url, filename, width, height) => {
  return new Promise((resolve, reject) => {
    https.get(url, (response) => {
      if (response.statusCode !== 200) {
        reject(new Error(`Failed to download ${url}: ${response.statusCode}`));
        return;
      }

      const chunks = [];
      response.on('data', (chunk) => chunks.push(chunk));
      response.on('end', () => {
        const buffer = Buffer.concat(chunks);
        const outputPath = path.join(__dirname, '../public/images', filename);

        // Optimize and resize the image
        sharp(buffer)
          .resize(width, height, {
            fit: 'cover',
            position: 'center'
          })
          .jpeg({ quality: 80 })
          .toFile(outputPath)
          .then(() => {
            console.log(`Downloaded and optimized ${filename}`);
            resolve();
          })
          .catch(reject);
      });
    }).on('error', reject);
  });
};

const downloadAllImages = async () => {
  try {
    // Create images directory if it doesn't exist
    const imagesDir = path.join(__dirname, '../public/images');
    if (!fs.existsSync(imagesDir)) {
      fs.mkdirSync(imagesDir, { recursive: true });
    }

    // Download all images
    await Promise.all(
      images.map(({ url, filename, width, height }) =>
        downloadImage(url, filename, width, height)
      )
    );

    console.log('All images downloaded and optimized successfully!');
  } catch (error) {
    console.error('Error downloading images:', error);
  }
};

downloadAllImages(); 