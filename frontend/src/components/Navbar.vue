<template>
  <nav class="fixed w-full top-0 z-40 bg-[var(--secondary-black)] text-[var(--accent-offwhite)]">
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center py-4">
        <!-- Logo & Home link -->
        <div>
          <router-link to="/" class="text-2xl font-bold" style="font-family: var(--font-title); color: var(--primary-gold);">
            Noir et Or
          </router-link>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:flex space-x-10">
          <router-link to="/" class="hover:text-[var(--primary-gold)] transition" style="font-family: var(--font-nav);">HOME</router-link>
          <router-link to="/menu" class="hover:text-[var(--primary-gold)] transition" style="font-family: var(--font-nav);">MENU</router-link>
          <router-link to="/reservations" class="hover:text-[var(--primary-gold)] transition" style="font-family: var(--font-nav);">RESERVATIONS</router-link>
          <router-link to="/contact" class="hover:text-[var(--primary-gold)] transition" style="font-family: var(--font-nav);">CONTACT</router-link>
        </div>

        <!-- Login/Profile Button -->
        <div>
          <button 
            v-if="!isLoggedIn" 
            @click="openLoginModal"
            class="text-[var(--primary-gold)] border border-[var(--primary-gold)] px-6 py-2 rounded-full hover:bg-[var(--primary-gold)] hover:text-[var(--secondary-black)] transition"
            style="font-family: var(--font-button);"
          >
            LOGIN
          </button>
          
          <div v-else class="relative">
            <button 
              @click="toggleProfileMenu"
              class="flex items-center text-[var(--primary-gold)]"
            >
              <img 
                v-if="user?.profile_picture || user?.picture" 
                :src="user?.profile_picture || user?.picture" 
                alt="Profile" 
                class="w-8 h-8 rounded-full mr-2"
              >
              <i v-else class="fas fa-user-circle mr-2 text-xl"></i>
              <span class="hidden md:inline-block" style="font-family: var(--font-body);">{{ user?.name || 'Account' }}</span>
              <i class="fas fa-chevron-down ml-2 text-xs"></i>
            </button>
            
            <div v-if="profileMenuOpen" class="absolute right-0 mt-2 w-48 bg-[var(--secondary-black)] border border-[var(--deep-charcoal)] rounded-md shadow-xl z-50">
              <div class="py-2">
                <a href="#" class="block px-4 py-2 hover:bg-[var(--deep-charcoal)] hover:text-[var(--primary-gold)]">My Profile</a>
                <a href="#" class="block px-4 py-2 hover:bg-[var(--deep-charcoal)] hover:text-[var(--primary-gold)]">My Reservations</a>
                <hr class="border-[var(--deep-charcoal)] my-1">
                <a @click.prevent="logout" href="#" class="block px-4 py-2 hover:bg-[var(--deep-charcoal)] hover:text-[var(--primary-gold)]">Sign Out</a>
              </div>
            </div>
          </div>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button @click="toggleMobileMenu" class="text-2xl">
            <i :class="mobileMenuOpen ? 'fas fa-times' : 'fas fa-bars'" class="text-[var(--primary-gold)]"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu -->
    <div v-if="mobileMenuOpen" class="md:hidden bg-[var(--deep-charcoal)] pt-4 pb-6 shadow-lg">
      <div class="container mx-auto px-4 flex flex-col space-y-4">
        <router-link to="/" class="hover:text-[var(--primary-gold)] transition py-2 border-b border-gray-700" 
          style="font-family: var(--font-nav);" @click="mobileMenuOpen = false">HOME</router-link>
        <router-link to="/menu" class="hover:text-[var(--primary-gold)] transition py-2 border-b border-gray-700" 
          style="font-family: var(--font-nav);" @click="mobileMenuOpen = false">MENU</router-link>
        <router-link to="/reservations" class="hover:text-[var(--primary-gold)] transition py-2 border-b border-gray-700" 
          style="font-family: var(--font-nav);" @click="mobileMenuOpen = false">RESERVATIONS</router-link>
        <router-link to="/contact" class="hover:text-[var(--primary-gold)] transition py-2" 
          style="font-family: var(--font-nav);" @click="mobileMenuOpen = false">CONTACT</router-link>
      </div>
    </div>
  </nav>
  
  <LoginModal ref="loginModal" />
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';
import { useAuthStore } from '@/stores/auth';
import LoginModal from './LoginModal.vue';

const loginModal = ref(null);
const mobileMenuOpen = ref(false);
const profileMenuOpen = ref(false);
const authStore = useAuthStore();

const isLoggedIn = computed(() => authStore.isLoggedIn);
const user = computed(() => authStore.user);

const openLoginModal = () => {
  loginModal.value?.openModal();
};

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value;
  if (mobileMenuOpen.value) {
    profileMenuOpen.value = false;
  }
};

const toggleProfileMenu = () => {
  profileMenuOpen.value = !profileMenuOpen.value;
};

const logout = () => {
  authStore.logout();
  profileMenuOpen.value = false;
};

// Close profile menu when clicking outside
const handleClickOutside = (event) => {
  if (profileMenuOpen.value && !event.target.closest('.relative')) {
    profileMenuOpen.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', handleClickOutside);
  
  // Listen for login success events
  window.eventBus.on('login:success', (data) => {
    console.log('Login success event received in Navbar.vue:', data);
    if (loginModal.value) {
      console.log('Forcing modal to close from Navbar.vue');
      
      // Make sure the navbar updates its auth state
      if (data.user) {
        console.log('Updating navbar user data');
      }
      
      // Apply additional DOM cleanup for all modals
      setTimeout(() => {
        document.querySelectorAll('.fixed.inset-0.flex.justify-center').forEach(modal => {
          console.log('Force cleanup of modal from Navbar.vue:', modal);
          modal.style.display = 'none';
        });
      }, 100);
    }
  });
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
  window.eventBus.off('login:success');
});
</script>