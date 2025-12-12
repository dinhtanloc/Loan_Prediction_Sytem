import axios from './axiosClient'

export function register(payload) {
  return axios.post('/auth/register', payload)
}

export function login(payload) {
  return axios.post('/auth/login', payload)
}

export function logout() {
  return axios.post('/auth/logout')
}
