<script setup>
import { ref } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
// If you have an API helper: import { login } from '@/api/client'

const router = useRouter()
const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

async function onSubmit() {
  error.value = ''
  loading.value = true
  try {
    // await login(username.value, password.value)
    // After success:
    router.push({ name: 'books' })
  } catch (e) {
    error.value = e?.message || 'Login failed'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="login-page">
    <h1>Login</h1>
    <form @submit.prevent="onSubmit">
      <label>Username</label>
      <input v-model="username" required />
      <label>Password</label>
      <input type="password" v-model="password" required />
      <button :disabled="loading">{{ loading ? '...' : 'Login' }}</button>
      <p v-if="error" style="color:red">{{ error }}</p>
    </form>
    <router-link to="/" class = "login-button">Login</router-link>
    <router-link to="/Register" class = "register-button">Register</router-link>
  </div>
</template>

<style scoped>

</style>