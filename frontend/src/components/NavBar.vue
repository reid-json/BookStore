<!--Setting up the global navbar component-->
<script>
export default {
  name: "NavBar",
};
</script>

<template>
<nav class="navbar">
  <div class="nav-left">
    My App
  </div>
  <div class="nav-right">
    <router-link to="/">Home</router-link>
    <router-link to="/Books">Books</router-link>
    <router-link to="/Login">Logout</router-link>
  </div>
</nav>
</template>

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
.nav-right{
  display: flex;
  gap: 1rem;
}
.nav-right a{
  text-decoration: none;
  color: #fff;
  font-weight: 500;
}
.nav-right a:hover{
  color: #007bff;
}
</style>