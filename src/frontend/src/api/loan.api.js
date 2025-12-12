import axios from './axiosClient'

export function predictLoan(payload) {
  return axios.post('/predict', payload)
}
