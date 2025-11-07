<template>
  <nav class="navbar">
    <div class="nav-left">
      <i class="fas fa-book-open"></i>
      <span class="brand">Shlves</span>
    </div>
    <div class="nav-right">
      <router-link to="/" class="nav-item">
        <i class="fas fa-home"></i>
        <span>Home</span>
      </router-link>
      <router-link to="/Books" class="nav-item">
        <i class="fas fa-book"></i>
        <span>Books</span>
      </router-link>
      <router-link to="/cart" class="nav-item">
        <i class="fas fa-shopping-cart"></i>
        <span>Cart</span>
      </router-link>
      <router-link to="/orders" class="nav-item">
        <i class="fas fa-box"></i>
        <span>My Orders</span>
      </router-link>
      <button @click="logout" class="nav-item logout-button">
        <i class="fas fa-sign-out-alt"></i>
        <span>Logout</span>
      </button>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
  methods: {
    logout() {
      localStorage.removeItem('authToken');
      this.$router.push('/Login');
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville&display=swap');

.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  width: 100%;
  background-color: #121212;
  color: #f0f0f0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 2rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.5);
  font-family: 'Libre Baskerville', serif;
  z-index: 1000;
}

.nav-left {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.4rem;
  font-weight: bold;
  color: #a0e0a0;
}

.brand {
  font-size: 1.2rem;
}

.nav-right {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #f0f0f0;
  text-decoration: none;
  font-size: 0.95rem;
  transition: color 0.3s ease;
  background: none;
  border: none;
  cursor: pointer;
}

.nav-item:hover {
  color: #a0e0a0;
}

.logout-button {
  font-family: inherit;
}
</style>