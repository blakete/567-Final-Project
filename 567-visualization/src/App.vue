<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <h1>The Relationship Between Exercise and Anxiety</h1>
    <div class="comboContainer">
      <ComboChart></ComboChart>
    </div>
    <div class="chartRow">
      <PieChart></PieChart>
      <RadarChart></RadarChart>
      <HeatmapChart></HeatmapChart>
    </div>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import PlanetChart from "@/components/PlanetChart.vue";
import PieChart from "./components/PieChart.vue";
import RadarChart from "@/components/RadarChart.vue";
import ComboChart from "@/components/ComboChart.vue";
import HeatmapChart from "@/components/HeatmapChart.vue";

export default {
  name: "App",
  components: {
    // HelloWorld,
    // PlanetChart,
    PieChart,
    RadarChart,
    ComboChart,
    HeatmapChart,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}

.chartRow {
  display: flex;
  width: 100%;
}

.comboContainer {
  margin-bottom: 20px;
}

</style>
