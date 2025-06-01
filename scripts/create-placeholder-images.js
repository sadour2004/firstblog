const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

const images = [
  {
    filename: 'hero-morocco.jpg',
    width: 1920,
    height: 1080,
    color: '#4A90E2' // Blue
  },
  {
    filename: 'tangier.jpg',
    width: 800,
    height: 600,
    color: '#50E3C2' // Teal
  },
  {
    filename: 'rabat.jpg',
    width: 800,
    height: 600,
    color: '#F5A623' // Orange
  },
  {
    filename: 'marrakech.jpg',
    width: 800,
    height: 600,
    color: '#D0021B' // Red
  },
  {
    filename: 'casablanca.jpg',
    width: 800,
    height: 600,
    color: '#9013FE' // Purple
  },
  {
    filename: 'fez.jpg',
    width: 800,
    height: 600,
    color: '#417505' // Green
  },
  {
    filename: 'marrakech-hidden.jpg',
    width: 800,
    height: 600,
    color: '#D0021B' // Red
  },
  {
    filename: 'tangier-beach.jpg',
    width: 800,
    height: 600,
    color: '#50E3C2' // Teal
  }
];

const createPlaceholderImage = async ({ filename, width, height, color }) => {
  const outputPath = path.join(__dirname, '../public/images', filename);
  
  // Create a solid color image
  await sharp({
    create: {
      width,
      height,
      channels: 4,
      background: { r: 0, g: 0, b: 0, alpha: 0 }
    }
  })
  .composite([{
    input: Buffer.from(`<svg><rect width="100%" height="100%" fill="${color}"/></svg>`),
    top: 0,
    left: 0,
  }])
  .jpeg({ quality: 80 })
  .toFile(outputPath);

  console.log(`Created placeholder image: ${filename}`);
};

const createAllPlaceholderImages = async () => {
  try {
    // Create images directory if it doesn't exist
    const imagesDir = path.join(__dirname, '../public/images');
    if (!fs.existsSync(imagesDir)) {
      fs.mkdirSync(imagesDir, { recursive: true });
    }

    // Create all placeholder images
    await Promise.all(
      images.map(image => createPlaceholderImage(image))
    );

    console.log('All placeholder images created successfully!');
  } catch (error) {
    console.error('Error creating placeholder images:', error);
  }
};

createAllPlaceholderImages(); 