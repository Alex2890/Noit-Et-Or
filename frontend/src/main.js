import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router';
import '@fortawesome/fontawesome-free/css/all.min.css';
import { createPinia } from 'pinia';
import vue3GoogleLogin from 'vue3-google-login';
import axios from 'axios';

// Create a global event bus
window.eventBus = {
  emit(event, data) {
    document.dispatchEvent(new CustomEvent(event, { detail: data }));
  },
  on(event, callback) {
    document.addEventListener(event, (e) => callback(e.detail));
  },
  off(event, callback) {
    document.removeEventListener(event, callback);
  }
};

// Configure axios for communication with backend
axios.defaults.baseURL = '';  // Use relative URLs for Vite proxy
axios.defaults.withCredentials = false;
axios.defaults.headers.common['Content-Type'] = 'application/json';

const app = createApp(App);
app.use(router);
app.use(createPinia());

// Register the vue3GoogleLogin plugin globally with FedCM support
app.use(vue3GoogleLogin, {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
  prompt: false, // Avoid consent prompts which may trigger FedCM errors
  itp_support: true, // Enable Intelligent Tracking Prevention support for Safari
  auto_select: true // Sometimes helps with FedCM flow
});

app.mount('#app');