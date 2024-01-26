<template>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <TestApi/>
</template>

<script>
import TestApi from './components/TestApi.vue'
// import UserLogin from './components/LoGin.vue' // Renamed from 'Login' to 'UserLogin'

export default {
  name: 'App',
  components: {
    TestApi // Updated component name
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
