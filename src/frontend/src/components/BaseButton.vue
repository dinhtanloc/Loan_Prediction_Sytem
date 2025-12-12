<template>
  <button v-bind="$attrs" class="base-button"><slot /></button>
</template>

<script setup>
</script>

<style scoped>
.base-button {
  background-color: #2563eb;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  border: none;
  cursor: pointer;
}
.base-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
</style>
