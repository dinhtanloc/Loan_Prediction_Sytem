<template>
  <div class="auth-layout">
    <main>
      <slot />
    </main>
  </div>
</template>

<style scoped>
.auth-layout { display:flex; align-items:center; justify-content:center; min-height:100vh; }
main { width:420px; padding:2rem; background:#fff; border-radius:8px; box-shadow:0 6px 18px rgba(0,0,0,0.06); }
</style>
