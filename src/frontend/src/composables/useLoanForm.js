import { reactive } from 'vue'

export function useLoanForm() {
  const form = reactive({
    credit_score: '',
    income: '',
    loan_amount: '',
    term: ''
  })

  function reset() {
    form.credit_score = ''
    form.income = ''
    form.loan_amount = ''
    form.term = ''
  }

  return { form, reset }
}
