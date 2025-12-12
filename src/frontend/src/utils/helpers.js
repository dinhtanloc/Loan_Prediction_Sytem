export function toNumber(v) {
  const n = Number(v)
  return Number.isFinite(n) ? n : null
}
