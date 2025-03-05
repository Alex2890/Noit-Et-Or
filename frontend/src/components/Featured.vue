<template>
    <section class="py-16 bg-[var(--accent-offwhite)]">
      <div class="container mx-auto px-4">
        <h2 class="text-5xl font-bold text-center mb-12" style="font-family: var(--font-title); color: var(--primary-gold);">
          Chef's Specialties
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            <div v-for="(image, index) in images" :key="index" class="relative group overflow-hidden rounded-xl shadow-lg">
                <img :src="image.src" :alt="image.alt" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" />
                <div class="absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition duration-500 flex items-center justify-center">
                    <h3 class="text-2xl text-white text-center" style="font-family: var(--font-title);">
                        {{ image.alt }}
                    </h3>
                </div>
            </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  // Import images using ES6 import
  import feature1 from '@/assets/featured/feature-1.jpg';
  import feature2 from '@/assets/featured/feature-2.jpg';
  import feature3 from '@/assets/featured/feature-3.jpg';
  import feature4 from '@/assets/featured/feature-4.jpg';
  import feature5 from '@/assets/featured/feature-5.jpg';
  import feature6 from '@/assets/featured/feature-6.jpg';
  
  // Array of images
  const images = [
    {
      src: feature1,
      alt: 'Gourmet Duck Breast with Cherries',
    },
    {
      src: feature2,
      alt: 'Italian Goat Cheese Appetizer',
    },
    {
      src: feature3,
      alt: 'Crispy Skin Fish Fillet',
    },
    {
      src: feature4,
      alt: 'Italian Seafood Delight',
    },
    {
      src: feature5,
      alt: 'Grilled Mushroom Dish',
    },
    {
      src: feature6,
      alt: 'Tiramisu Dessert',
    }
  ];
  </script>
  