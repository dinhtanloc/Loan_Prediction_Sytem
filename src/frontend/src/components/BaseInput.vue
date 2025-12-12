<template>
  <input v-bind="$attrs" v-model="modelValue" @input="$emit('update:modelValue', modelValue)" class="base-input" />
</template>

<script setup>
defineProps({ modelValue: [String, Number] })
const emit = defineEmits(['update:modelValue'])
let modelValue = undefined
</script>

<style scoped>
.base-input {
  padding: 0.5rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
  width: 100%;
  box-sizing: border-box;
}
</style>
