<template>
  <div class="container">
    <h2>Register</h2>
    <form @submit.prevent="onSubmit">
      <label>Username</label>
      <input v-model="username" required />
      <label>Email</label>
      <input v-model="email" type="email" />
      <label>Password</label>
      <input type="password" v-model="password" required minlength="8" />
      <button :disabled="loading">{{ loading ? '...' : 'Create account' }}</button>
      <p v-if="error" style="color:red">{{ error }}</p>
      <p v-if="ok" style="color:green">Account created. You can log in now.</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { registerUser } from '@/api/client'

const username = ref('')
const email = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')
const ok = ref(false)

async function onSubmit() {
  error.value = ''; ok.value = false; loading.value = true
  try {
    await registerUser({ username: username.value, email: email.value, password: password.value })
    ok.value = true
  } catch (e) {
    error.value = e.message || 'Registration failed'
  } finally {
    loading.value = false
  }
}
</script>