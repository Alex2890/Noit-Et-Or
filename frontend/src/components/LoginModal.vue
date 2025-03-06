<template>
    <div class="modal" v-if="showModal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>Login</h2>
        <form @submit.prevent="login">
          <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" required>
          </div>
          <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required>
          </div>
          <button type="submit">Login</button>
        </form>
        <div class="social-login">
          <GoogleLogin
            :callback="handleGoogleLoginSuccess"
            :prompt="true"
            @error="handleGoogleLoginError"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const showModal = ref(false);
  const email = ref('');
  const password = ref('');
  
  const openModal = () => {
    showModal.value = true;
  };
  
  const closeModal = () => {
    showModal.value = false;
  };
  
  const login = () => {
    // Handle email/password login here
    console.log('Email:', email.value);
    console.log('Password:', password.value);
    closeModal();
  };
  
  const handleGoogleLoginSuccess = (response) => {
    console.log('Google login success:', response);
    // Send the Google token to your backend for verification
  };
  
  const handleGoogleLoginError = (error) => {
    console.error('Google login error:', error);
  };
  
  defineExpose({ openModal });
  </script>
  
  <style scoped>
  /* Add your modal styles here */
  </style>