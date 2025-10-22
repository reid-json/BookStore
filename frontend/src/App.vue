<script>
import NavBar from "./components/NavBar.vue";
import { useRoute } from "vue-router";
import { computed } from "vue";

export default {
  components: {
    NavBar
  },
  computed: {
    hideNavBar(){
      return this.$route.path === '/Login';
    }
  }
}

</script>

<template>
  <div id="app">
    <NavBar v-if ="!hideNavBar"/>
    <router-view />
  </div>

</template>

<style scoped>

</style>
