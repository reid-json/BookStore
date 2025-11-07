<template>
  <div class="login-container">
    <h1>Login</h1>
    <form @submit.prevent="onSubmit">
      <label for="username">Username</label>
      <input id="username" v-model="username" required />

      <label for="password">Password</label>
      <input id="password" type="password" v-model="password" required />

      <button :disabled="loading">{{ loading ? 'Logging in...' : 'Login' }}</button>

      <p v-if="error" class="error">{{ error }}</p>
    </form>

    <div class="links">
      <RouterLink to="/Register">Register</RouterLink>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

async function onSubmit() {
  error.value = ''
  loading.value = true
  try {
    const response = await fetch('http://127.0.0.1:8000/auth/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    })

    const contentType = response.headers.get('content-type')
    const raw = await response.text()

    if (!response.ok) {
      if (contentType && contentType.includes('application/json')) {
        const errData = JSON.parse(raw)
        throw new Error(errData.detail || 'Login failed')
      } else {
        throw new Error('Unexpected server response')
      }
    }

    const data = JSON.parse(raw)
    localStorage.setItem('authToken', data.access)
    router.push('/')
  } catch (e) {
    error.value = e.message
    console.error('Login error:', e)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
:root{
  text-decoration-color: #181818;

}

.login-container {
  max-width: 400px;
  margin: 80px auto;
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: #f9f9f9;
}

h1 {
  text-align: center;
  margin-bottom: 1.5rem;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 1rem;
  font-weight: bold;
}

input {
  padding: 0.5rem;
  font-size: 1rem;
  margin-top: 0.25rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  margin-top: 1.5rem;
  padding: 0.75rem;
  font-size: 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #aaa;
  cursor: not-allowed;
}

.error {
  color: red;
  margin-top: 1rem;
  text-align: center;
}

.links {
  margin-top: 1rem;
  text-align: center;
}
</style>