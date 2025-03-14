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
import { ref, onMounted, watch } from 'vue';
import { useAuthStore } from '@/stores/auth';
import Hero from "@/components/Hero.vue";
import Featured from "@/components/Featured.vue";
import AboutUs from "@/components/AboutUs.vue";
import OurChefStory from "@/components/OurChefStory.vue";
import PrivateEvents from "@/components/PrivateEvents.vue";
import LoginModal from '@/components/LoginModal.vue';

const loginModal = ref(null);

const authStore = useAuthStore();

// Add a watcher for auth state changes
watch(() => authStore.isLoggedIn, (newValue) => {
  console.log('Auth state changed in Home.vue:', newValue);
  if (newValue && loginModal.value) {
    console.log('User now logged in, modal should be closed');
    // Don't call closeModal directly as it may not be exposed
    // The login.success event handles closing properly
  }
}, { immediate: true });

onMounted(() => {
  console.log('Home component mounted, auth state:', authStore.isLoggedIn);
  
  // Add event listener for login success
  window.eventBus.on('login:success', (data) => {
    console.log('Login success event received in Home.vue:', data);
    if (loginModal.value) {
      console.log('Forcing modal to close from Home.vue');
      // DOM-based approach instead of calling a method
      document.querySelectorAll('.login-modal-container').forEach(modal => {
        console.log('Force cleanup of modal from Home.vue DOM:', modal);
        modal.style.display = 'none';
      });
      
      // Apply an additional DOM cleanup
      setTimeout(() => {
        document.querySelectorAll('.fixed.inset-0.flex.justify-center').forEach(modal => {
          console.log('Force cleanup of modal from Home.vue:', modal);
          modal.style.display = 'none';
        });
      }, 100);
    }
  });
  
  // Only show login modal if user is not logged in
  if (!authStore.isLoggedIn && loginModal.value) {
    console.log('User not logged in, opening login modal');
    // If not logged in and modal ref is available, open the login modal
    setTimeout(() => {
      loginModal.value?.openModal();
    }, 500); // Small delay to ensure component is fully mounted
  } else {
    console.log('User already logged in, not showing login modal');
  }
});
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