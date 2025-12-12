import { defineStore } from 'pinia'

export const useLoanStore = defineStore('loan', {
  state: () => ({
    result: null,
    loading: false
  }),
  actions: {
    setResult(r) {
      this.result = r
    },
    setLoading(v) {
      this.loading = v
    }
  }
})
