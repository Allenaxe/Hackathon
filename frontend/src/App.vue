<template>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <TestApi/>
</template>

<script>
import TestApi from './components/TestApi.vue'

export default {
  name: 'App',
  components: {
    TestApi
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
