<template>
  <input 
    v-bind="$attrs"
    :value="modelValue"
    @input="onInput"
    class="base-input"
  />
</template>

<script setup>
const props = defineProps({
  modelValue: [String, Number]
})
const emit = defineEmits(['update:modelValue'])

function onInput(e) {
  emit('update:modelValue', e.target.value)
}
</script>

<style scoped>
.base-input {
  padding: 0.5rem 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 6px;
}
</style>
