<template>
  <nav class="bg-[var(--deep-charcoal)] text-[var(--primary-gold)] fixed w-full top-0 z-50 shadow-lg border-b border-[var(--primary-gold)]">
    <div class="max-w-7xl mx-auto px-6 lg:px-12">
      <div class="flex justify-between items-center h-20">
        <!-- Logo / Brand Name -->
        <div class="flex items-center">
          <h1 class="text-4xl font-extrabold tracking-wide" style="font-family: var(--font-title);">
            Noir et Or
          </h1>
        </div>

        <!-- Desktop Navigation + Login Button -->
        <div class="hidden md:flex space-x-8 items-center">
          <router-link
            to="/"
            class="text-lg uppercase tracking-wider transition duration-300 hover:text-[var(--hover-darkgold)]"
            active-class="active-link"
            exact-active-class="active-link"
            style="font-family: var(--font-button);"
          >
            Home
          </router-link>
          <router-link
            to="/menu"
            class="text-lg uppercase tracking-wider transition duration-300 hover:text-[var(--hover-darkgold)]"
            active-class="active-link"
            exact-active-class="active-link"
            style="font-family: var(--font-button);"
          >
            Menu
          </router-link>
          <router-link
            to="/reservations"
            class="text-lg uppercase tracking-wider transition duration-300 hover:text-[var(--hover-darkgold)]"
            active-class="active-link"
            exact-active-class="active-link"
            style="font-family: var(--font-button);"
          >
            Reservations
          </router-link>
          <router-link
            to="/contact"
            class="text-lg uppercase tracking-wider transition duration-300 hover:text-[var(--hover-darkgold)]"
            active-class="active-link"
            exact-active-class="active-link"
            style="font-family: var(--font-button);"
          >
            Contact
          </router-link>
          <!-- Login Button beside Contact Tab -->
          <LoginButton />
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button @click="toggleMenu" class="text-3xl hover:text-[var(--hover-darkgold)] focus:outline-none">
            ☰
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu (Hidden by Default) -->
    <div v-if="mobileMenuOpen" class="md:hidden absolute top-20 left-0 w-full bg-black text-center py-4 shadow-lg border-t border-[var(--primary-gold)]">
      <router-link
        to="/"
        class="block py-3 text-lg uppercase tracking-wider transition hover:text-[var(--hover-darkgold)]"
        active-class="active-link"
        exact-active-class="active-link"
        style="font-family: var(--font-button);"
      >
        Home
      </router-link>
      <router-link
        to="/menu"
        class="block py-3 text-lg uppercase tracking-wider transition hover:text-[var(--hover-darkgold)]"
        active-class="active-link"
        exact-active-class="active-link"
        style="font-family: var(--font-button);"
      >
        Menu
      </router-link>
      <router-link
        to="/reservations"
        class="block py-3 text-lg uppercase tracking-wider transition hover:text-[var(--hover-darkgold)]"
        active-class="active-link"
        exact-active-class="active-link"
        style="font-family: var(--font-button);"
      >
        Reservations
      </router-link>
      <router-link
        to="/contact"
        class="block py-3 text-lg uppercase tracking-wider transition hover:text-[var(--hover-darkgold)]"
        active-class="active-link"
        exact-active-class="active-link"
        style="font-family: var(--font-button);"
      >
        Contact
      </router-link>
      <!-- Login Button in Mobile Menu -->
      <div class="py-3">
        <LoginButton />
      </div>
    </div>

    <!-- Scroll to Top Button -->
    <button
      v-show="showScrollToTop"
      @click="scrollToTop"
      class="fixed bottom-6 left-6 p-3 rounded-full bg-[var(--primary-gold)] text-[var(--secondary-black)] shadow-lg transition-transform transform hover:scale-110 focus:outline-none"
      style="z-index: 60;"
      title="Scroll to Top"
    >
      <i class="fas fa-arrow-up text-2xl font-bold"></i>
    </button>
  </nav>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from "vue";
import LoginButton from './LoginButton.vue'; // Importing Login Button Component

const mobileMenuOpen = ref(false);
const showScrollToTop = ref(false);

const toggleMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value;
};

const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
};

const handleScroll = () => {
  showScrollToTop.value = window.scrollY > 300;
};

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onBeforeUnmount(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>
