import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router';
import '@fortawesome/fontawesome-free/css/all.min.css';
import { createPinia } from 'pinia';
import vue3GoogleLogin from 'vue3-google-login';

const app = createApp(App);
app.use(router);
app.use(createPinia());

// Register the vue3GoogleLogin plugin globally
app.use(vue3GoogleLogin, {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
});

app.mount('#app');