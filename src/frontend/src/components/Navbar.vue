<template>
  <nav class="nav">
    <div class="brand">LoanApp</div>
    <div class="links">
      <router-link to="/">Home</router-link>
      <router-link to="/loan">Predict</router-link>
      <button v-if="isAuth" @click="doLogout">Logout</button>
      <router-link v-else to="/login">Login</router-link>
    </div>
  </nav>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '@/store/auth.store'

const store = useAuthStore()
const isAuth = computed(() => store.isAuthenticated)

function doLogout() {
  store.clear()
}
</script>
