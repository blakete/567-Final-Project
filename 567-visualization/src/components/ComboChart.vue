<template>
  <div class="chartContainer">
    <canvas id="combo-chart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";
import comboChartData from "@/data/combo-data.js";

export default {
  name: "ComboChart",
  data() {
    return {
      comboChartData: comboChartData,
    };
  },
  computed: {},
  mounted() {
    const ctx = document.getElementById("combo-chart");
    new Chart(ctx, this.comboChartData);
  },
};
</script>

<style scoped>
.chartContainer {
  position: relative;
  height: 45vh;
  width: 97vw;
}
</style>