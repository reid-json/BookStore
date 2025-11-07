<template>
  <div class="register-container">
    <h2>Create Your Account</h2>
    <form @submit.prevent="onSubmit">
      <label>Username</label>
      <input v-model="username" required />

      <label>Email</label>
      <input v-model="email" type="email" />

      <label>Password</label>
      <input type="password" v-model="password" required minlength="8" />

      <button :disabled="loading">{{ loading ? '...' : 'Create Account' }}</button>

      <p v-if="error" class="error">{{ error }}</p>
      <p v-if="ok" class="success">Account created. You can log in now.</p>
    </form>

    <button class="login-btn" @click="goToLogin">Go to Login</button>
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

function goToLogin() {
  router.push('/Login')
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

.register-container {
  max-width: 420px;
  margin: 100px auto;
  padding: 2rem;
  background-color: #1e1e1e;
  border-radius: 10px;
  box-shadow: 0 0 20px rgba(160, 224, 160, 0.2);
  font-family: 'Libre Baskerville', serif;
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

h2 {
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
  font-weight: bold;
  color: #ccc;
}

input {
  padding: 0.6rem;
  font-size: 1rem;
  margin-top: 0.25rem;
  border: 1px solid #444;
  border-radius: 6px;
  background-color: #121212;
  color: #f0f0f0;
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

.login-btn {
  margin-top: 1.5rem;
  background-color: #a0e0a0;
  color: #121212;
}

.login-btn:hover {
  background-color: #8cd88c;
}

.error {
  color: #ff6b6b;
  margin-top: 1rem;
  text-align: center;
  font-size: 0.95rem;
}

.success {
  color: #a0e0a0;
  margin-top: 1rem;
  text-align: center;
  font-size: 0.95rem;
}
</style>