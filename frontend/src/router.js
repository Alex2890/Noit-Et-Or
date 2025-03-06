// src/router.js
import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Menu from "@/views/Menu.vue";
import Reservations from "@/views/Reservations.vue";
import Contact from "@/views/Contact.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/menu", name: "Menu", component: Menu },
  { path: "/reservations", name: "Reservations", component: Reservations },
  { path: "/contact", name: "Contact", component: Contact },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
