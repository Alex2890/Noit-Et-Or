<template>
  <section>
    <!-- Hero Image Section -->
    <div 
      class="relative w-full min-h-screen bg-cover bg-center flex flex-col items-center justify-center"
      :style="heroBackgroundStyle"
    >
      <div class="text-center text-[var(--primary-gold)]">
        <h1 
          class="text-6xl font-bold mb-4 drop-shadow-lg" 
          style="font-family: var(--font-title); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);"
        >
          Private Events at Noir et Or
        </h1>
        <p 
          class="text-2xl mb-8 text-[var(--text-white)] font-semibold drop-shadow-md" 
          style="font-family: var(--font-button); text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.6);"
        >
          Celebrate in style and elegance. <br />
          Whether it's an intimate gathering or a grand celebration, we make every moment unforgettable.
        </p>
        <!-- Inquire Now Button Linked to Contact Page -->
        <button
        @click="goToContact"
        class="px-6 py-4 bg-[var(--primary-gold)] text-[var(--secondary-black)] text-lg font-semibold rounded-lg transition transform hover:scale-105 hover:shadow-xl hover:underline"
        style="font-family: var(--font-button);"
      >
        Inquire Now
      </button>
      </div>
    </div>

    <!-- Event Highlights Gallery -->
    <section class="py-16 bg-[var(--accent-offwhite)] text-center">
      <div class="container mx-auto">
        <!-- Section Title -->
        <h2 class="text-4xl font-bold mb-12 text-[var(--primary-gold)]" style="font-family: var(--font-title);">
          Event Highlights
        </h2>

        <!-- Image Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div 
            v-for="(image, index) in eventImages" 
            :key="index" 
            class="relative group overflow-hidden rounded-xl shadow-lg"
          >
            <img 
              :src="image.src" 
              :alt="image.alt" 
              class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
            />
            <div 
              class="absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition duration-500 flex items-center justify-center"
            >
              <h3 class="text-2xl text-white" style="font-family: var(--font-title);">
                {{ image.alt }}
              </h3>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Detail Shots Section -->
    <section class="py-16 bg-[var(--bg-deep-burgundy-light)] text-center">
      <div class="container mx-auto">
        <!-- Section Title -->
        <h2 class="text-4xl font-bold mb-12 text-[var(--primary-gold)]" style="font-family: var(--font-title);">
          Exquisite Details
        </h2>

        <!-- Detail Shots Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-8">
          <div class="overflow-hidden rounded-lg shadow-lg">
            <img 
              :src="detailImages[0].src" 
              :alt="detailImages[0].alt" 
              class="w-full h-full object-cover"
            />
          </div>
          <div class="overflow-hidden rounded-lg shadow-lg">
            <img 
              :src="detailImages[1].src" 
              :alt="detailImages[1].alt" 
              class="w-full h-full object-cover"
            />
          </div>
        </div>
      </div>
    </section>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router';
// ES6 Import for Hero Image
import heroImage from '@/assets/private-events/private-1.jpg';

// Event Highlights Gallery Images
import private2 from '@/assets/private-events/private-2.jpg';
import private3 from '@/assets/private-events/private-3.jpg';
import private4 from '@/assets/private-events/private-4.jpg';
import private5 from '@/assets/private-events/private-5.jpg';
import private6 from '@/assets/private-events/private-6.jpg';
import private7 from '@/assets/private-events/private-7.jpg';

// Detail Shots
import private8 from '@/assets/private-events/private-8.jpg';
import private9 from '@/assets/private-events/private-9.jpg';

// Hero Background Style
const heroBackgroundStyle = `background-image: url('${heroImage}'); background-size: cover; background-position: center;`;

// Event Highlights Gallery Images Array
const eventImages = [
  {
    src: private2,
    alt: 'Elegant Table Setting',
  },
  {
    src: private3,
    alt: 'Intimate Dining Ambiance',
  },
  {
    src: private4,
    alt: 'Luxury Banquet Arrangement',
  },
  {
    src: private5,
    alt: 'Celebration Table Decor',
  },
  {
    src: private6,
    alt: 'Grand Dining Hall',
  },
  {
    src: private7,
    alt: 'Floral Table Centerpiece',
  }
];

// Detail Shots Array
const detailImages = [
  {
    src: private8,
    alt: 'Luxury Dining Setup',
  },
  {
    src: private9,
    alt: 'Sophisticated Table Arrangement',
  }
];

// Programmatic Navigation to Reservations Page
const router = useRouter();
const goToContact = () => {
router.push('/contact');
};
</script>
