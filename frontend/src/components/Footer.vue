<template>
    <footer class="bg-[var(--deep-charcoal)] text-[var(--text-white)] py-8">
      <div class="container mx-auto text-center space-y-4">
        <!-- Brand Name -->
        <h1 class="text-4xl font-bold" style="font-family: var(--font-title);">
          Noir et Or
        </h1>
  
        <!-- Quick Links with Active Underline and Scroll to Top -->
        <div class="space-x-6" style="font-family: var(--font-button);">
          <router-link 
            to="/" 
            class="text-[var(--primary-gold)] hover:text-[var(--hover-darkgold)] transition"
            :class="{ 'text-[var(--hover-darkgold)] underline': $route.path === '/' }"
            @click.native="scrollToTop"
          >Home</router-link>
          <router-link 
            to="/menu" 
            class="text-[var(--primary-gold)] hover:text-[var(--hover-darkgold)] transition"
            :class="{ 'text-[var(--hover-darkgold)] underline': $route.path === '/menu' }"
            @click.native="scrollToTop"
          >Menu</router-link>
          <router-link 
            to="/reservations" 
            class="text-[var(--primary-gold)] hover:text-[var(--hover-darkgold)] transition"
            :class="{ 'text-[var(--hover-darkgold)] underline': $route.path === '/reservations' }"
            @click.native="scrollToTop"
          >Reservations</router-link>
          <router-link 
            to="/contact" 
            class="text-[var(--primary-gold)] hover:text-[var(--hover-darkgold)] transition"
            :class="{ 'text-[var(--hover-darkgold)] underline': $route.path === '/contact' }"
            @click.native="scrollToTop"
          >Contact</router-link>
        </div>
  
        <!-- Contact Information -->
        <div class="text-sm text-[var(--text-white)]" style="font-family: var(--font-button);">
          123 Noir St, Culinary City<br />
          Phone: +1 234 567 890<br />
          Email: info@noiretorn.com
        </div>
  
        <!-- Social Media Icons -->
        <div class="flex justify-center space-x-6 text-2xl">
          <a href="#" class="text-[var(--primary-gold)] hover:text-[var(--hover-darkgold)] transition" aria-label="Facebook">
            <i class="fab fa-facebook"></i>
          </a>
          <a href="#" class="text-[var(--primary-gold)] hover:text-[var(--hover-darkgold)] transition" aria-label="Instagram">
            <i class="fab fa-instagram"></i>
          </a>
          <a href="#" class="text-[var(--primary-gold)] hover:text-[var(--hover-darkgold)] transition" aria-label="LinkedIn">
            <i class="fab fa-linkedin"></i>
          </a>
        </div>
  
        <!-- Copyright Notice -->
        <p class="text-xs mt-4 text-[var(--text-white)]" style="font-family: var(--font-button);">
          © 2025 Noir et Or. All rights reserved.
        </p>
      </div>
    </footer>
  </template>
  
  <script setup>
  import { onMounted } from "vue";
  import { useRouter } from "vue-router";
  
  const router = useRouter();
  
  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };
  
  // Scroll to top on route change
  onMounted(() => {
    router.afterEach(() => {
      scrollToTop();
    });
  });
  </script>
  