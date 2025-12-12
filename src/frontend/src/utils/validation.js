export function required(v) {
  return v !== null && v !== undefined && String(v).trim().length > 0
}

export function isEmail(v) {
  return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(String(v))
}
