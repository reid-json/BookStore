<template>
  <nav class="navbar">
    <div class="nav-left">
      My App
    </div>
    <div class="nav-right">
      <router-link to="/">Home</router-link>
      <router-link to="/Books">Books</router-link>
      <router-link to="/cart">Cart</router-link>
      <router-link to="/orders">My Orders</router-link>
      <button @click="logout" class="logout-button">Logout</button>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
    logout() {
      localStorage.removeItem('authToken') // 🔐 Clear token
      this.$router.push('/Login')          // 🔁 Redirect to login
    }
  }
}
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  background-color: #000;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  z-index: 1000;
}
.nav-right {
  display: flex;
  gap: 1rem;
}
.nav-right a,
.logout-button {
  text-decoration: none;
  color: #fff;
  font-weight: 500;
  background: none;
  border: none;
  cursor: pointer;
}
.nav-right a:hover,
.logout-button:hover {
  color: #007bff;
}
</style>