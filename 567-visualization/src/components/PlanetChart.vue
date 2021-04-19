<template>
  <div>
    <canvas id="planet-chart" :width="width" :height="height"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js'
import planetChartData from '@/data/planet-data.js'

export default {
  name: 'PlanetChart',
  props: ['width', 'height'],
  data() {
    return {
      planetChartData: planetChartData
    }
  },
  mounted() {
    const ctx = document.getElementById('planet-chart');
    new Chart(ctx, this.planetChartData);
  }
}
</script>