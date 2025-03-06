<template>
  <div v-if="isVisible" class="fixed inset-0 flex justify-center items-center bg-opacity-50 backdrop-blur-md z-50">
    <div class="bg-[var(--accent-offwhite)] p-6 rounded-lg w-full max-w-sm shadow-lg relative">
      <button @click="closeModal" class="absolute top-3 right-3 text-black text-xl">&times;</button>
      <h1 class="text-3xl text-center mb-6" style="font-family: var(--font-title); color: var(--primary-gold);">
        Noir et Or
      </h1>
      <div class="space-y-3">
        <button class="w-full flex items-center justify-center bg-[var(--primary-gold)] text-[var(--secondary-black)] py-2 px-4 rounded-lg transition hover:bg-[var(--hover-darkgold)]" @click="loginWithGoogle">
          <span>CONTINUE WITH</span>
          <i class="fab fa-google pl-2"></i>
        </button>
        <button class="w-full flex items-center justify-center bg-[var(--primary-gold)] text-[var(--secondary-black)] py-2 px-4 rounded-lg transition hover:bg-[var(--hover-darkgold)]" @click="loginWithFacebook">
          <span>CONTINUE WITH</span>
          <i class="fab fa-facebook pl-2"></i>
        </button>
        <div class="my-4 flex items-center">
          <div class="border-t border-gray-300 flex-1"></div>
          <span class="mx-3 text-black">or</span>
          <div class="border-t border-gray-300 flex-1"></div>
        </div>
        <form @submit.prevent="login">
          <div class="mb-4">
            <label for="email" class="text-sm text-[var(--deep-charcoal)]" style="font-family: var(--font-body);">Email *</label>
            <input
              type="email"
              id="email"
              placeholder="Enter your email"
              class="block w-full px-3 py-2 mt-1 bg-white text-[var(--deep-charcoal)] border border-gray-300 rounded-lg focus:outline-none focus:border-[var(--primary-gold)]"
              v-model="email"
              style="font-family: var(--font-body);"
            />
          </div>
          <div class="mb-7 relative">
            <label for="password" class="text-sm text-[var(--deep-charcoal)]" style="font-family: var(--font-body);">Password *</label>
            <input
              :type="passwordVisible ? 'text' : 'password'"
              id="password"
              placeholder="Enter your password"
              class="block w-full px-3 py-2 mt-1 bg-white text-[var(--deep-charcoal)] border border-gray-300 rounded-lg focus:outline-none focus:border-[var(--primary-gold)]"
              v-model="password"
              style="font-family: var(--font-body);"
            />
            <button type="button" class="absolute right-3 top-10 text-black" @click="togglePasswordVisibility">
              <i :class="passwordVisible ? 'fas fa-eye' : 'fas fa-eye-slash'"></i>
            </button>
          </div>
          <button
            type="submit"
            class="w-full py-2 bg-[var(--primary-gold)] text-[var(--secondary-black)] text-lg font-semibold rounded-lg transition transform hover:bg-[var(--hover-darkgold)]"
            style="font-family: var(--font-button); text-transform: uppercase; letter-spacing: 2px;"
          >
            Log In
          </button>
        </form>
        <div class="mt-4 text-center">
          <a href="#" style="color: var(--primary-gold); font-family: var(--font-body);" class="text-lg hover:text-[var(--hover-darkgold)]">Forgot password?</a>
        </div>
        <div class="mt-2 text-center">
          <span class="text-lg text-[var(--deep-charcoal)]" style="font-family: var(--font-body);">New to Noir et Or?</span>
          <a href="#" style="color: var(--primary-gold); font-family: var(--font-body);" class="text-lg hover:underline ml-1">Sign Up</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

const authStore = useAuthStore();

const isVisible = ref(false);
const passwordVisible = ref(false);
const email = ref('');
const password = ref('');

const togglePasswordVisibility = () => {
  passwordVisible.value = !passwordVisible.value;
};

const openModal = () => {
  isVisible.value = true;
};

const closeModal = () => {
  isVisible.value = false;
};

const login = async () => {
  try {
    const response = await axios.post('/api/login', {
      email: email.value,
      password: password.value,
    });
    const token = response.data.token;
    const user = jwtDecode(token);

    authStore.setToken(token);
    authStore.setUser(user);

    closeModal();
  } catch (error) {
    console.error('Login error:', error);
  }
};

const loginWithGoogle = () => {
  console.log('Google login clicked');
};

const loginWithFacebook = () => {
  console.log('Facebook login clicked');
};

defineExpose({ openModal });
</script>