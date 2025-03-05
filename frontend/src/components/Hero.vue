<template>
  <section
    class="relative w-full min-h-screen bg-cover bg-center flex flex-col items-center justify-center"
    :style="backgroundStyle"
  >
    <div class="text-center text-[var(--primary-gold)]">
      <h1 
        class="text-6xl font-bold mb-4 drop-shadow-lg" 
        style="font-family: var(--font-title); text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);"
      >
        A Taste of Elegance
      </h1>
      <p 
        class="text-2xl mb-8 text-[var(--text-white)] drop-shadow-md" 
        style="font-family: var(--font-body); text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.6);"
      >
        Indulge in a luxurious dining experience where gourmet flavors meet sophistication.
      </p>
      
      <!-- Button to Navigate to Reservations Page -->
      <button
        @click="goToReservations"
        class="px-6 py-4 bg-[var(--primary-gold)] text-[var(--secondary-black)] text-lg font-semibold rounded-lg transition transform hover:scale-105 hover:shadow-xl hover:underline"
        style="font-family: var(--font-button);"
      >
        Reserve Your Table
      </button>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router';
import heroImage from '@/assets/hero-image.jpg';

// Use the imported image as the background directly
const backgroundStyle = `background-image: url('${heroImage}'); background-size: cover; background-position: center;`;

// Programmatic Navigation to Reservations Page
const router = useRouter();

const goToReservations = () => {
  router.push('/reservations');
};
</script>
