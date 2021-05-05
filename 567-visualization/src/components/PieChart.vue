<template>
  <div class="chartContainer">
    <canvas id="pie-chart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

export default {
  name: "PieChart",
  data() {
    return {
      pieChartData: {
        type: "pie",
        data: {
          labels: ["Inside", "Outside"],
          datasets: [
            {
              label: "My First Dataset",
              data: [37, 117],
              backgroundColor: [
                "rgb(255, 99, 132)",
                "rgb(54, 162, 235)"
              ],
              hoverOffset: 4,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          title: {
            display: true,
            text: "Inside vs. Outside Workout Duration Total",
            fontSize: 25,
          },
          legend: {
            position: "bottom",
          },
        },
      },
    };
  },
  computed: {
    style() {
      return "background-color: " + this.hovering ? this.color : "red";
    },
  },
  mounted() {
    const ctx = document.getElementById("pie-chart");
    new Chart(ctx, this.pieChartData);
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
