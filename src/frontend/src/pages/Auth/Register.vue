<template>
  <AuthLayout>
    <h2>Register</h2>
    <form @submit.prevent="onSubmit">
      <BaseInput v-model="name" placeholder="Full name" />
      <BaseInput v-model="email" placeholder="Email" />
      <BaseInput v-model="password" placeholder="Password" type="password" />
      <BaseButton :disabled="loading">Register</BaseButton>
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

const name = ref('')
const email = ref('')
const password = ref('')
const loading = ref(false)
const { register } = useAuth()
const router = useRouter()

async function onSubmit() {
  loading.value = true
  try {
    const res = await register({ name: name.value, email: email.value, password: password.value })
    if (res && res.status === 201) {
      router.push({ name: 'Login' })
    }
  } finally {
    loading.value = false
  }
}
</script>
