<template>
  <!-- Background Overlay -->
  <div v-if="isVisible" class="fixed inset-0 flex justify-center items-center bg-opacity-50 backdrop-blur-md z-50">
    
    <!-- Modal Box -->
    <div class="bg-white p-6 rounded-lg w-full max-w-sm shadow-lg relative">
      
      <!-- Close Button -->
      <button @click="closeModal" class="absolute top-3 right-3 text-black text-xl">&times;</button>
      
      <!-- Title -->
      <h1 class="text-3xl text-center mb-6" style="font-family: var(--font-title); color: var(--primary-gold);">
        Noir et Or
      </h1>

      <!-- Social Sign-In Buttons -->
      <div class="space-y-3">
      <!-- Google Sign-In Button -->
        <button class="w-full flex items-center justify-center bg-[var(--primary-gold)] text-[var(--secondary-black)] py-2 px-4 rounded-lg transition hover:shadow-lg">
          <span>CONTINUE WITH</span>
          <i class="fab fa-google pl-2"></i>
        </button>

      <!-- Facebook Sign-In Button -->
        <button class="w-full flex items-center justify-center bg-[var(--primary-gold)] text-[var(--secondary-black)] py-2 px-4 rounded-lg transition hover:shadow-lg">
          <span>CONTINUE WITH</span>
          <i class="fab fa-facebook pl-2"></i>
        </button>

      <!-- Twitter/X Sign-In Button -->
        <button class="w-full flex items-center justify-center bg-[var(--primary-gold)] text-[var(--secondary-black)] py-2 px-4 rounded-lg transition hover:shadow-lg">
          <span>CONTINUE WITH</span>
          <i class="fab fa-x-twitter pl-2"></i>
        </button>
      </div>

      <!-- Divider -->
      <div class="my-4 flex items-center">
        <div class="border-t border-gray-300 flex-1"></div>
        <span class="mx-3 text-black">or</span>
        <div class="border-t border-gray-300 flex-1"></div>
      </div>

      <!-- Email and Password Fields -->
      <form class="space-y-3">
        <div>
          <label for="email" class="text-sm text-black">Email *</label>
          <input
            type="email"
            id="email"
            placeholder="Enter your email"
            class="block w-full px-3 py-2 mt-1 bg-white text-black border border-gray-300 rounded-lg focus:outline-none focus:border-[var(--primary-gold)]"
          />
        </div>

        <div class="relative">
          <label for="password" class="text-sm text-black">Password *</label>
          <input
            :type="passwordVisible ? 'text' : 'password'"
            id="password"
            placeholder="Enter your password"
            class="block w-full px-3 py-2 mt-1 bg-white text-black border border-gray-300 rounded-lg focus:outline-none focus:border-[var(--primary-gold)]"
          />
          <button type="button" class="absolute right-3 top-9 text-black" @click="togglePasswordVisibility">
            <i :class="passwordVisible ? 'fas fa-eye' : 'fas fa-eye-slash'"></i>
          </button>
        </div>

        <!-- Sign In Button -->
        <button
          type="submit"
          class="w-full py-3 bg-[var(--primary-gold)] text-[var(--secondary-black)] text-lg font-semibold rounded-lg transition transform hover:scale-105 hover:shadow-xl hover:underline"
        >
          Sign In
        </button>
      </form>

      <!-- Links -->
      <div class="mt-4 text-center">
        <a href="#" class="text-sm text-black hover:text-[var(--primary-gold)]">Forgot password?</a>
      </div>
      <div class="mt-2 text-center">
        <span class="text-sm text-black">New to Noir et Or?</span>
        <a href="#" class="text-sm text-black hover:underline ml-1">Sign Up</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineExpose } from 'vue';

const isVisible = ref(false);
const passwordVisible = ref(false);

const togglePasswordVisibility = () => {
  passwordVisible.value = !passwordVisible.value;
};

const openModal = () => {
  isVisible.value = true;
};

const closeModal = () => {
  isVisible.value = false;
};

// Expose functions so they can be called from LoginButton.vue
defineExpose({ openModal });
</script>

<style scoped>
/* Additional styling if needed */
</style>
