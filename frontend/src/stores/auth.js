import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => {
    // Try to recover user from localStorage if exists
    let savedUser = null;
    try {
      const savedUserString = localStorage.getItem('user');
      if (savedUserString) {
        savedUser = JSON.parse(savedUserString);
      }
    } catch (e) {
      console.error('Error parsing saved user:', e);
    }
    
    return {
      token: localStorage.getItem('token') || null,
      user: savedUser,
    };
  },
  getters: {
    isLoggedIn: (state) => !!state.token,
  },
  actions: {
    setToken(token) {
      console.log('Setting token in auth store');
      this.token = token;
      localStorage.setItem('token', token); // Store the token in localStorage
    },
    setUser(user) {
      console.log('Setting user in auth store:', user);
      this.user = user;
      // Save user to localStorage for persistence
      if (user) {
        localStorage.setItem('user', JSON.stringify(user));
      }
    },
    logout() {
      console.log('Logging out');
      this.token = null;
      this.user = null;
      localStorage.removeItem('token'); // Remove the token from localStorage
      localStorage.removeItem('user'); // Remove the user from localStorage
    },
  },
});