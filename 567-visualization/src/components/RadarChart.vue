<template>
  <div class="chartContainer">
    <canvas id="radar-chart"></canvas>
  </div>
</template>

<script>
import Chart from "chart.js";

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

export default {
  name: "RadarChart",
  data() {
    return {
      radarChartData: {
        type: "polarArea",
        data: {
          labels: ["Walk", "Run", "Strength", "Cycle"],
          datasets: [
            {
              label: "My First Dataset",
              data: [0.5932112259682684, 0.2359570718498529, 0.15939779892542208, 0.01143390325645686],
              backgroundColor: [
                "rgb(255, 99, 132)",
                "rgb(75, 192, 192)",
                "rgb(245, 230, 66)",
                "rgb(201, 203, 207)",
                "rgb(245, 167, 66)",
                "rgb(54, 162, 235)",
              ],
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          title: {
            display: true,
            text: "Exercise Type by Calories Burned",
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
    const ctx = document.getElementById("radar-chart");
    new Chart(ctx, this.radarChartData);
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
