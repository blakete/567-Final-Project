<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1>The Relationship Between Exercise and Anxiety</h1>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <PlanetChart :width="500" :height="200"></PlanetChart>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import PlanetChart from '@/components/PlanetChart.vue'

export default {
  name: 'App',
  components: {
    // HelloWorld,
    PlanetChart
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
