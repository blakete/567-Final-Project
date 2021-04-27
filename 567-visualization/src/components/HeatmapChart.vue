<template>
  <div class="chartContainer">
    <canvas id="heatmap-chart"></canvas>
  </div>
</template>

<script>
import heatmapChartData from "@/data/heatmap-data.js";
import Chart from "chart.js";

export default {
  name: "HeatmapChart",
  components: {},
  data: () => {
    return {
      heatmapChartData: heatmapChartData,
    };
  },
  computed: {},
  mounted() {
    const ctx = document.getElementById("heatmap-chart");
    new Chart(ctx, this.heatmapChartData);
  },
};
</script>

<style scoped>
.chartContainer {
  position: relative; 
  height: 40vh; 
  width: 33vw;
}
</style>
