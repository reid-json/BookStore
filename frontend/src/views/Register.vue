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

    <!-- 🔹 Login Button -->
    <button @click="goToLogin" style="margin-top: 1rem">Go to Login</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const username = ref('')
const email = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')
const ok = ref(false)

async function onSubmit() {
  error.value = ''
  ok.value = false
  loading.value = true

  try {
    const response = await fetch('http://127.0.0.1:8000/auth/register/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        email: email.value,
        password: password.value
      })
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || 'Registration failed')
    }

    ok.value = true
  } catch (e) {
    error.value = e.message || 'Registration failed'
  } finally {
    loading.value = false
  }
}

// 🔹 Login Button Handler
function goToLogin() {
  router.push('/Login')
}
</script>