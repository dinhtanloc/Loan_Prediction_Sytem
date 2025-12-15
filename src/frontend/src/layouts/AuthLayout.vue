<template>
  <div class="auth-layout">
    <main>
      <slot />
    </main>
  </div>
</template>

<script setup>
</script>

<style scoped>
.auth-layout {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 1rem;
}

main {[]
  width: 100%;
  max-width: 420px;
  background: #fff;
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}
</style>
