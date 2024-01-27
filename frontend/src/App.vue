<template>
<<<<<<< Updated upstream
  <router-view />
=======
   <button v-if="$route.path !== '/login' && $route.path !== '/register'" @click="goToAboutPage">About Us</button>
  <router-view></router-view>
>>>>>>> Stashed changes
</template>

<script>

export default {
  name: 'App',
<<<<<<< Updated upstream
  components: {
  }
=======
  methods: {
    goToAboutPage() {
      this.$router.push("/login");
    },
  },
>>>>>>> Stashed changes
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
