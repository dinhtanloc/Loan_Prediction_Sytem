<template>
  <div>
    <Navbar />
    <div class="container">
      <slot />
    </div>
  </div>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue'
</script>

<style scoped>
.container { padding:1.25rem; }
</style>
