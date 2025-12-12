import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/pages/Home.vue'
import Login from '@/pages/Auth/Login.vue'
import Register from '@/pages/Auth/Register.vue'
import ForgotPassword from '@/pages/Auth/ForgotPassword.vue'
import LoanPrediction from '@/pages/Loan/LoanPrediction.vue'
import { useAuthStore } from '@/store/auth.store'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/login', name: 'Login', component: Login, meta: { public: true } },
  { path: '/register', name: 'Register', component: Register, meta: { public: true } },
  { path: '/forgot', name: 'Forgot', component: ForgotPassword, meta: { public: true } },
  { path: '/loan', name: 'Loan', component: LoanPrediction, meta: { requiresAuth: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const store = useAuthStore()
  if (to.meta.requiresAuth && !store.isAuthenticated) {
    next({ name: 'Login' })
    return
  }
  if (to.meta.public && store.isAuthenticated) {
    next({ name: 'Loan' })
    return
  }
  next()
})

export default router
