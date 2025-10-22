<template>
  <div class="container">
    <h2>Login</h2>
    <form @submit.prevent="onSubmit">
      <label>Username</label>
      <input v-model="username" required />
      <label>Password</label>
      <input type="password" v-model="password" required />
      <button :disabled="loading">{{ loading ? '...' : 'Login' }}</button>
      <p v-if="error" style="color:red">{{ error }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { login, me } from '@/api/client'

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

async function onSubmit() {
  error.value = ''; loading.value = true
  try {
    await login(username.value, password.value)
    await me()
    window.location.href = '/'
  } catch (e) {
    error.value = e.message || 'Login failed'
  } finally {
    loading.value = false
  }
}
</script>