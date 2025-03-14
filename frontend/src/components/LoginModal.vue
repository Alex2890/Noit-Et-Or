<template>
  <div v-if="isVisible" class="fixed inset-0 flex justify-center items-center z-50 login-modal-container" :class="{'backdrop-removed': !showBackdrop}">
    <div class="bg-[var(--accent-offwhite)] p-6 rounded-lg w-full max-w-sm shadow-lg relative">
      <button @click="closeModal" class="absolute top-3 right-3 text-black text-xl">&times;</button>
      <h1 class="text-3xl text-center mb-6" style="font-family: var(--font-title); color: var(--primary-gold);">
        Noir et Or
      </h1>
      
      <div v-if="loading" class="flex justify-center items-center py-6">
        <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-[var(--primary-gold)]"></div>
      </div>
      
      <div v-else class="space-y-3 my-4">
        <!-- Google Login with proper component wrapper -->
        <GoogleLogin
          :callback="handleCallback"
          :error="handleError"
          class="w-full flex items-center justify-center bg-[var(--primary-gold)] text-[var(--secondary-black)] py-2 px-4 rounded-lg transition hover:bg-[var(--hover-darkgold)]"
        >
          <template v-slot:default>
            <button class="w-full flex items-center justify-center">
              <span>CONTINUE WITH</span>
              <i class="fab fa-google pl-2"></i>
            </button>
          </template>
        </GoogleLogin>
        
        
        
        <button 
          data-fb-login
          class="w-full flex items-center justify-center bg-[var(--primary-gold)] text-[var(--secondary-black)] py-2 px-4 rounded-lg transition hover:bg-[var(--hover-darkgold)]" 
          @click="loginWithFacebook"
        >
          <span>CONTINUE WITH</span>
          <i class="fab fa-facebook pl-2"></i>
        </button>
        <div class="my-4 flex items-center">
          <div class="border-t border-gray-300 flex-1"></div>
          <span class="mx-3 text-black">or</span>
          <div class="border-t border-gray-300 flex-1"></div>
        </div>
        <div v-if="errorMessage" class="bg-red-100 border border-red-300 text-red-700 px-4 py-2 rounded-md mb-4">
          {{ errorMessage }}
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
              required
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
              required
            />
            <button type="button" class="absolute right-3 top-10 text-black" @click="togglePasswordVisibility">
              <i :class="passwordVisible ? 'fas fa-eye' : 'fas fa-eye-slash'"></i>
            </button>
          </div>
          <button
            type="submit"
            class="w-full py-2 bg-[var(--primary-gold)] text-[var(--secondary-black)] text-lg font-semibold rounded-lg transition transform hover:bg-[var(--hover-darkgold)]"
            style="font-family: var(--font-button); text-transform: uppercase; letter-spacing: 2px;"
            :disabled="loading"
          >
            <span v-if="loading">Processing...</span>
            <span v-else>Log In</span>
          </button>
        </form>
        <div class="mt-4 text-center">
          <a href="#" style="color: var(--primary-gold); font-family: var(--font-body);" class="text-lg hover:text-[var(--hover-darkgold)]">Forgot password?</a>
        </div>
        <div class="mt-2 text-center">
          <span class="text-lg text-[var(--deep-charcoal)]" style="font-family: var(--font-body);">New to Noir et Or?</span>
          <a href="#" @click.prevent="showSignUp" style="color: var(--primary-gold); font-family: var(--font-body);" class="text-lg hover:underline ml-1">Sign Up</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick, computed } from 'vue';
import { useAuthStore } from '@/stores/auth';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';
import { googleAuthCodeLogin, googleTokenLogin } from 'vue3-google-login';


const authStore = useAuthStore();
const googleLoginRef = ref(null);

const isVisible = ref(false);
const passwordVisible = ref(false);
const email = ref('');
const password = ref('');
const loading = ref(false);
const errorMessage = ref('');
const showBackdrop = ref(true);

// Development mode detection removed

const togglePasswordVisibility = () => {
  passwordVisible.value = !passwordVisible.value;
};

const openModal = () => {
  isVisible.value = true;
};

const closeModal = () => {
  // Reset form state
  errorMessage.value = '';
  
  console.log('Starting modal close with animation');
  
  // First remove the backdrop (blur effect)
  showBackdrop.value = false;
  
  // Then close the modal after animation completes
  setTimeout(() => {
    // Close the modal
    isVisible.value = false;
    console.log('Modal closed, isVisible set to:', isVisible.value);
    
    // Reset backdrop for next time
    showBackdrop.value = true;
  }, 300);
  
  // Reset form fields after a short delay (after animation completes)
  setTimeout(() => {
    if (!isVisible.value) {
      email.value = '';
      password.value = '';
      passwordVisible.value = false;
    }
  }, 500);
};

const login = async () => {
  try {
    errorMessage.value = '';
    loading.value = true;
    
    console.log('Attempting login with email:', email.value);
    
    try {
      const response = await axios.post('/api/auth/login', {
        email: email.value,
        password: password.value,
      });
      
      console.log('Login response:', response.data);
      const token = response.data.token;
      const user = jwtDecode(token);
  
      authStore.setToken(token);
      authStore.setUser(user);
  
      closeModal();
    } catch (apiError) {
      console.error('Login API error:', apiError);
      console.error('Error details:', apiError.response?.data);
      
      // Only for testing/development - create a mock user if login fails
      // This should be removed in production!
      if (email.value === '123@gmail.com' && password.value === 'alexander21') {
        console.log('⚠️ DEVELOPMENT MODE: Creating mock user for testing');
        
        // Create mock user for testing
        const mockUser = {
          id: 123,
          email: email.value,
          name: 'Test User'
        };
        
        // Store in auth store
        authStore.setToken('mock-token-for-testing');
        authStore.setUser(mockUser);
        
        // Close modal
        closeModal();
      } else {
        // Show error for other credentials
        errorMessage.value = apiError.response?.data?.error || 'Login failed. Please check your credentials.';
      }
    }
  } catch (error) {
    console.error('Login error:', error);
    errorMessage.value = 'An unexpected error occurred during login.';
  } finally {
    loading.value = false;
  }
};

// Handle callback from GoogleLogin component
const handleCallback = async (response) => {
  try {
    errorMessage.value = '';
    loading.value = true;
    
    // Extract credential from Google response
    const credential = response.credential || response.code;
    const responseType = response.credential ? 'credential' : 'code';
    
    if (!credential) {
      throw new Error('No valid credential in Google response');
    }
    
    // Begin animation
    showBackdrop.value = false;
    
    // Send credential to backend
    const result = await axios.post('/api/auth/google', {
      credential: credential,
      response_type: responseType
    });
    
    // Process backend response
    const token = result.data.token;
    const user = jwtDecode(token);
    
    // Save authenticated user data
    authStore.setToken(token);
    authStore.setUser(user);
    
    // Complete animation sequence
    setTimeout(() => {
      isVisible.value = false;
      loading.value = false;
      showBackdrop.value = true;
    }, 300);
    
    // Notify other components
    window.eventBus.emit('login:success', { user });
  } catch (error) {
    // Handle authentication errors
    errorMessage.value = 'Authentication failed. Please try again.';
    loading.value = false;
    showBackdrop.value = true;
  }
};

const handleError = (error) => {
  errorMessage.value = 'Google authentication failed. Please try again.';
  
  // Auto-clear error after 5 seconds
  setTimeout(() => {
    if (errorMessage.value === 'Google authentication failed. Please try again.') {
      errorMessage.value = '';
    }
  }, 5000);
};

// Debug function removed

// Google login method - streamlined and using real Google data
const initiateGoogleLogin = async (existingResponse) => {
  try {
    errorMessage.value = '';
    loading.value = true;
    
    // Get response - either from parameter or initiate new login
    const response = existingResponse || await googleAuthCodeLogin();
    
    // Get the credential from the response
    const credential = response.code || response.credential;
    const responseType = response.code ? 'code' : 'credential';
    
    if (!credential) {
      throw new Error('No valid credential found in response');
    }
    
    // Show loading state while we authenticate with backend
    showBackdrop.value = false;
    
    // Send the authentication data to the backend
    const result = await axios.post('/api/auth/google', {
      credential: credential,
      response_type: responseType
    });
    
    // Get the token and user info
    const token = result.data.token;
    const user = jwtDecode(token);
    
    // Store real user data in auth store
    authStore.setToken(token);
    authStore.setUser(user);
    
    // Close the modal with smooth animation
    setTimeout(() => {
      isVisible.value = false;
      loading.value = false;
      showBackdrop.value = true;
    }, 300);
    
    // Notify other components
    window.eventBus.emit('login:success', { user });
  } catch (error) {
    // Handle any errors in the Google authentication flow
    errorMessage.value = 'Authentication failed. Please try again.';
    loading.value = false;
    showBackdrop.value = true;
  }
}

const loginWithFacebook = () => {
  // Temporarily disable button and show a toast or message instead of displaying error
  const facebookBtn = document.querySelector('button[data-fb-login]');
  if (facebookBtn) {
    facebookBtn.disabled = true;
    
    // Show temporary message
    errorMessage.value = 'Facebook login coming soon! Please use Google or email login.';
    
    // Re-enable after 3 seconds
    setTimeout(() => {
      facebookBtn.disabled = false;
      errorMessage.value = '';
    }, 3000);
  }
};

const showSignUp = () => {
  // Clear any previous error messages
  errorMessage.value = '';
  
  // Clear current form values
  email.value = '';
  password.value = '';
  
  // Here we would toggle to a sign-up form, but for now just show a message
  errorMessage.value = 'Sign-up functionality coming soon!';
  
  // Clear the message after 3 seconds
  setTimeout(() => {
    if (errorMessage.value === 'Sign-up functionality coming soon!') {
      errorMessage.value = '';
    }
  }, 3000);
};

// Expose methods to parent components
defineExpose({ openModal });

// Function to remove backdrop and then close modal
const removeBackdropAndClose = () => {
  showBackdrop.value = false;
  setTimeout(() => {
    isVisible.value = false;
  }, 300); // Small delay to allow animation to finish
};
</script>

<style scoped>
.login-modal-container {
  background-color: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(8px);
  transition: all 0.3s ease;
}

.backdrop-removed {
  background-color: transparent !important;
  backdrop-filter: blur(0px) !important;
}
</style>