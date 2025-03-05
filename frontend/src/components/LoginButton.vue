<template>
  <div>
    <!-- Login Button -->
    <button
      @click="openUserModal"
      class="px-4 py-2 bg-[var(--primary-gold)] text-[var(--secondary-black)] text-lg font-semibold rounded-lg transition transform hover:scale-105 hover:shadow-xl hover:underline"
    >
      Log In
    </button>

    <!-- Mount the modal component inside the same template -->
    <UserView ref="userModalRef" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import UserView from '@/views/Userview.vue';

const userModalRef = ref(null);

const openUserModal = () => {
  if (userModalRef.value) {
    userModalRef.value.openModal();
  }
};
</script>
