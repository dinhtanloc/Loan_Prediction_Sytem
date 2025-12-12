<template>
  <AuthLayout>
    <h2>Sign in</h2>
    <form @submit.prevent="onSubmit">
      <BaseInput v-model="email" placeholder="Email" />
      <BaseInput v-model="password" placeholder="Password" type="password" />
      <BaseButton :disabled="loading">Sign in</BaseButton>
    </form>
  </AuthLayout>
</template>

<script setup>
import { ref } from 'vue'
import AuthLayout from '@/layouts/AuthLayout.vue'
import BaseInput from '@/components/BaseInput.vue'
import BaseButton from '@/components/BaseButton.vue'
import { useAuth } from '@/composables/useAuth'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const loading = ref(false)
const { login } = useAuth()
const router = useRouter()

async function onSubmit() {
  loading.value = true
  try {
    const res = await login({ email: email.value, password: password.value })
    if (res && res.data && res.data.token) {
      router.push({ name: 'Loan' })
    }
  } finally {
    loading.value = false
  }
}
</script>
