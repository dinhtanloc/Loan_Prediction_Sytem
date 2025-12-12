<template>
  <AuthLayout>
    <h2>Forgot password</h2>
    <form @submit.prevent="onSubmit">
      <BaseInput v-model="email" placeholder="Email" />
      <BaseButton :disabled="loading">Send reset</BaseButton>
    </form>
  </AuthLayout>
</template>

<script setup>
import { ref } from 'vue'
import AuthLayout from '@/layouts/AuthLayout.vue'
import BaseInput from '@/components/BaseInput.vue'
import BaseButton from '@/components/BaseButton.vue'

const email = ref('')
const loading = ref(false)

async function onSubmit() {
  loading.value = true
  try {
  } finally {
    loading.value = false
  }
}
</script>
