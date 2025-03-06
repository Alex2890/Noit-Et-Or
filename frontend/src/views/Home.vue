<template>
  <div class="home">
    <LoginModal ref="loginModal" />
    <Hero />
    <AboutUs />
    <OurChefStory />
    <Featured />
    <PrivateEvents />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Hero from "@/components/Hero.vue";
import Featured from "@/components/Featured.vue";
import AboutUs from "@/components/AboutUs.vue";
import OurChefStory from "@/components/OurChefStory.vue";
import PrivateEvents from "@/components/PrivateEvents.vue";
import LoginModal from '@/components/LoginModal.vue';

const loginModal = ref(null);

onMounted(() => {
  // Check if the user is already logged in (you'll need to implement this logic)
  const isLoggedIn = checkIfLoggedIn(); // Replace with your authentication check

  if (!isLoggedIn) {
    // If not logged in, open the login modal
    loginModal.value.openModal();
  }
});

const checkIfLoggedIn = () => {
  const token = localStorage.getItem('token');
  return !!token; // Returns true if a token exists, false otherwise
};
</script>

<style scoped>
.home {
  /* Existing styles */
}

.home-content {
  filter: blur(5px); /* Blur the background when the modal is open */
  pointer-events: none; /* Prevent interaction with the background */
}
</style>