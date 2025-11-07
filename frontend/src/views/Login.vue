<template>
  <div class="login-container">
    <h1>Login to Shlves</h1>
    <form @submit.prevent="onSubmit">
      <label for="username">Username</label>
      <input id="username" v-model="username" required />

      <label for="password">Password</label>
      <input id="password" type="password" v-model="password" required />

      <button :disabled="loading">{{ loading ? 'Logging in...' : 'Login' }}</button>

      <p v-if="error" class="error">{{ error }}</p>
    </form>

    <div class="links">
      <RouterLink to="/Register">Don't have an account? Register</RouterLink>
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
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&display=swap');

.login-container {
  max-width: 420px;
  margin: 100px auto;
  padding: 2rem;
  background-color: #424242;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(160, 224, 160, 0.2);
  font-family: 'Quicksand', serif;
  color: #f0f0f0;
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

h1 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 1.5rem;
  color: #a0e0a0;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-top: 1rem;
  color: #a0e0a0;
}

input {
  padding: 0.6rem;
  font-size: 1rem;
  margin-top: 0.25rem;
  border: 1px solid #444;
  border-radius: 6px;
  background-color: #ffffff;
  color: #121212;
  transition: border-color 0.3s ease;
}

input:focus {
  outline: none;
  border-color: #a0e0a0;
  box-shadow: 0 0 5px rgba(160, 224, 160, 0.5);
}

button {
  margin-top: 1.5rem;
  padding: 0.75rem;
  font-size: 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-family: inherit;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #388e3c;
}

button:disabled {
  background-color: #666;
  cursor: not-allowed;
}

.error {
  color: #ff6b6b;
  margin-top: 1rem;
  text-align: center;
  font-size: 0.95rem;
}

.links {
  margin-top: 1.5rem;
  text-align: center;
}

.links a {
  color: #a0e0a0;
  text-decoration: none;
  font-weight: bold;
  transition: color 0.3s ease;
}

.links a:hover {
  color: #8cd88c;
}
</style>