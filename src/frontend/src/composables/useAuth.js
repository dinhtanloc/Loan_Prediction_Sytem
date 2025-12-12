import { ref } from 'vue'
import { useAuthStore } from '@/store/auth.store'
import * as api from '@/api/auth.api'

export function useAuth() {
  const store = useAuthStore()
  const error = ref(null)

  async function login(payload) {
    error.value = null
    const res = await api.login(payload)
    if (res && res.data && res.data.token) {
      store.setToken(res.data.token)
      store.setUser(res.data.user || null)
    }
    return res
  }

  async function register(payload) {
    error.value = null
    const res = await api.register(payload)
    return res
  }

  function logout() {
    store.clear()
    api.logout()
  }

  return { login, register, logout, error }
}
