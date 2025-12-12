<template>
  <MainLayout>
    <h2>Loan prediction</h2>
    <form @submit.prevent="onPredict">
      <BaseInput v-model="form.credit_score" placeholder="Credit score" />
      <BaseInput v-model="form.income" placeholder="Income" />
      <BaseInput v-model="form.loan_amount" placeholder="Loan amount" />
      <BaseInput v-model="form.term" placeholder="Term" />
      <BaseButton :disabled="loading">Predict</MainLayout>
    </form>
    <div v-if="result">Result: {{ result }}</div>
  </MainLayout>
</template>

<script setup>
import MainLayout from '@/layouts/MainLayout.vue'
import BaseInput from '@/components/BaseInput.vue'
import BaseButton from '@/components/BaseButton.vue'
import { useLoanForm } from '@/composables/useLoanForm'
import { predictLoan } from '@/api/loan.api'
import { useLoanStore } from '@/store/loan.store'

const { form } = useLoanForm()
const loan = useLoanStore()
const loading = loan.loading
const result = loan.result

async function onPredict() {
  loan.setLoading(true)
  try {
    const res = await predictLoan(form)
    if (res && res.data) loan.setResult(res.data)
  } finally {
    loan.setLoading(false)
  }
}
</script>
