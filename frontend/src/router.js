// src/router.js
import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Home.vue";
import Menu from "@/views/Menu.vue";
import Reservations from "@/views/Reservations.vue";
import Contact from "@/views/Contact.vue";
import UserView from "@/views/UserView.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/menu", name: "Menu", component: Menu },
  { path: "/reservations", name: "Reservations", component: Reservations },
  { path: "/contact", name: "Contact", component: Contact },
  { path: "/userview", name: "UserView", component: UserView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
