export const heatmapChartData = {
  type: "bubble",
  data: {
    datasets: [{
      label: 'First Dataset',
      // (1,1) = Sunday, 12 am
      // (1,3) = Sunday, 2 am
      // (2,3) = Monday, 2 am
      data: [

        // SUNDAY
        { // 12 am - 2 am
          x: 1,
          y: 1,
          r: 15
        },
        { // 2 am - 4 am
          x: 1,
          y: 3,
          r: 10
        },
        { // 4 am - 6 am
          x: 1,
          y: 5,
          r: 15
        },
        { // 6 am - 8 am
          x: 1,
          y: 7,
          r: 10
        },
        { // 8 am - 10 am
          x: 1,
          y: 9,
          r: 15
        },
        { // 10 am - 12 pm
          x: 1,
          y: 11,
          r: 10
        },
        { // 12 pm - 2 pm
          x: 1,
          y: 13,
          r: 15
        },
        { // 2 pm - 4 pm
          x: 1,
          y: 15,
          r: 10
        },
        { // 4 pm - 6 pm
          x: 1,
          y: 17,
          r: 10
        },
        { // 6 pm - 8 pm
          x: 1,
          y: 19,
          r: 10
        },
        { // 8 pm - 10 pm
          x: 1,
          y: 21,
          r: 10
        },
        { // 10 pm - 12 am
          x: 1,
          y: 23,
          r: 10
        },

        // MONDAY
        { // 12 am - 2 am
          x: 2,
          y: 1,
          r: 15
        },
        { // 2 am - 4 am
          x: 2,
          y: 3,
          r: 10
        },
        { // 4 am - 6 am
          x: 2,
          y: 5,
          r: 15
        },
        { // 6 am - 8 am
          x: 2,
          y: 7,
          r: 10
        },
        { // 8 am - 10 am
          x: 2,
          y: 9,
          r: 15
        },
        { // 10 am - 12 pm
          x: 2,
          y: 11,
          r: 10
        },
        { // 12 pm - 2 pm
          x: 2,
          y: 13,
          r: 15
        },
        { // 2 pm - 4 pm
          x: 2,
          y: 15,
          r: 10
        },
        { // 4 pm - 6 pm
          x: 2,
          y: 17,
          r: 10
        },
        { // 6 pm - 8 pm
          x: 2,
          y: 19,
          r: 10
        },
        { // 8 pm - 10 pm
          x: 2,
          y: 21,
          r: 10
        },
        { // 10 pm - 12 am
          x: 2,
          y: 23,
          r: 10
        },

        // TUESDAY
        { // 12 am - 2 am
          x: 3,
          y: 1,
          r: 15
        },
        { // 2 am - 4 am
          x: 3,
          y: 3,
          r: 10
        },
        { // 4 am - 6 am
          x: 3,
          y: 5,
          r: 15
        },
        { // 6 am - 8 am
          x: 3,
          y: 7,
          r: 10
        },
        { // 8 am - 10 am
          x: 3,
          y: 9,
          r: 15
        },
        { // 10 am - 12 pm
          x: 3,
          y: 11,
          r: 10
        },
        { // 12 pm - 2 pm
          x: 3,
          y: 13,
          r: 15
        },
        { // 2 pm - 4 pm
          x: 3,
          y: 15,
          r: 10
        },
        { // 4 pm - 6 pm
          x: 3,
          y: 17,
          r: 10
        },
        { // 6 pm - 8 pm
          x: 3,
          y: 19,
          r: 10
        },
        { // 8 pm - 10 pm
          x: 3,
          y: 21,
          r: 10
        },
        { // 10 pm - 12 am
          x: 3,
          y: 23,
          r: 10
        },

        // WEDNESDAY
        { // 12 am - 2 am
          x: 4,
          y: 1,
          r: 15
        },
        { // 2 am - 4 am
          x: 4,
          y: 3,
          r: 10
        },
        { // 4 am - 6 am
          x: 4,
          y: 5,
          r: 15
        },
        { // 6 am - 8 am
          x: 4,
          y: 7,
          r: 10
        },
        { // 8 am - 10 am
          x: 4,
          y: 9,
          r: 15
        },
        { // 10 am - 12 pm
          x: 4,
          y: 11,
          r: 10
        },
        { // 12 pm - 2 pm
          x: 4,
          y: 13,
          r: 15
        },
        { // 2 pm - 4 pm
          x: 4,
          y: 15,
          r: 10
        },
        { // 4 pm - 6 pm
          x: 4,
          y: 17,
          r: 10
        },
        { // 6 pm - 8 pm
          x: 4,
          y: 19,
          r: 10
        },
        { // 8 pm - 10 pm
          x: 4,
          y: 21,
          r: 10
        },
        { // 10 pm - 12 am
          x: 4,
          y: 23,
          r: 10
        },

        // THURSDAY
        { // 12 am - 2 am
          x: 5,
          y: 1,
          r: 15
        },
        { // 2 am - 4 am
          x: 5,
          y: 3,
          r: 10
        },
        { // 4 am - 6 am
          x: 5,
          y: 5,
          r: 15
        },
        { // 6 am - 8 am
          x: 5,
          y: 7,
          r: 10
        },
        { // 8 am - 10 am
          x: 5,
          y: 9,
          r: 15
        },
        { // 10 am - 12 pm
          x: 5,
          y: 11,
          r: 10
        },
        { // 12 pm - 2 pm
          x: 5,
          y: 13,
          r: 15
        },
        { // 2 pm - 4 pm
          x: 5,
          y: 15,
          r: 10
        },
        { // 4 pm - 6 pm
          x: 5,
          y: 17,
          r: 10
        },
        { // 6 pm - 8 pm
          x: 5,
          y: 19,
          r: 10
        },
        { // 8 pm - 10 pm
          x: 5,
          y: 21,
          r: 10
        },
        { // 10 pm - 12 am
          x: 5,
          y: 23,
          r: 10
        },

        // FRIDAY
        { // 12 am - 2 am
          x: 6,
          y: 1,
          r: 15
        },
        { // 2 am - 4 am
          x: 6,
          y: 3,
          r: 10
        },
        { // 4 am - 6 am
          x: 6,
          y: 5,
          r: 15
        },
        { // 6 am - 8 am
          x: 6,
          y: 7,
          r: 10
        },
        { // 8 am - 10 am
          x: 6,
          y: 9,
          r: 15
        },
        { // 10 am - 12 pm
          x: 6,
          y: 11,
          r: 10
        },
        { // 12 pm - 2 pm
          x: 6,
          y: 13,
          r: 15
        },
        { // 2 pm - 4 pm
          x: 6,
          y: 15,
          r: 10
        },
        { // 4 pm - 6 pm
          x: 6,
          y: 17,
          r: 10
        },
        { // 6 pm - 8 pm
          x: 6,
          y: 19,
          r: 10
        },
        { // 8 pm - 10 pm
          x: 6,
          y: 21,
          r: 10
        },
        { // 10 pm - 12 am
          x: 6,
          y: 23,
          r: 10
        },

        // SATURDAY
        { // 12 am - 2 am
          x: 7,
          y: 1,
          r: 15
        },
        { // 2 am - 4 am
          x: 7,
          y: 3,
          r: 10
        },
        { // 4 am - 6 am
          x: 7,
          y: 5,
          r: 15
        },
        { // 6 am - 8 am
          x: 7,
          y: 7,
          r: 10
        },
        { // 8 am - 10 am
          x: 7,
          y: 9,
          r: 15
        },
        { // 10 am - 12 pm
          x: 7,
          y: 11,
          r: 10
        },
        { // 12 pm - 2 pm
          x: 7,
          y: 13,
          r: 15
        },
        { // 2 pm - 4 pm
          x: 7,
          y: 15,
          r: 10
        },
        { // 4 pm - 6 pm
          x: 7,
          y: 17,
          r: 10
        },
        { // 6 pm - 8 pm
          x: 7,
          y: 19,
          r: 10
        },
        { // 8 pm - 10 pm
          x: 7,
          y: 21,
          r: 10
        },
        { // 10 pm - 12 am
          x: 7,
          y: 23,
          r: 10
        },

        // PLACEHOLDER
        { // 12 am - 2 am
          x: 8,
          y: 1,
          r: 0
        },
        { // 2 am - 4 am
          x: 8,
          y: 3,
          r: 0
        },
        { // 4 am - 6 am
          x: 8,
          y: 5,
          r: 0
        },
        { // 6 am - 8 am
          x: 8,
          y: 7,
          r: 0
        },
        { // 8 am - 10 am
          x: 8,
          y: 9,
          r: 0
        },
        { // 10 am - 12 pm
          x: 8,
          y: 11,
          r: 0
        },
        { // 12 pm - 2 pm
          x: 8,
          y: 13,
          r: 0
        },
        { // 2 pm - 4 pm
          x: 8,
          y: 15,
          r: 0
        },
        { // 4 pm - 6 pm
          x: 8,
          y: 17,
          r: 0
        },
        { // 6 pm - 8 pm
          x: 8,
          y: 19,
          r: 0
        },
        { // 8 pm - 10 pm
          x: 8,
          y: 21,
          r: 0
        },
        { // 10 pm - 12 am
          x: 8,
          y: 23,
          r: 0
        },

      ],
      backgroundColor: 'rgb(255, 99, 132)'
    }],
    labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    title: {
      display: true,
      text: "Workouts by Time of Day",
      fontSize: 25,
    },
    legend: {
      position: "bottom",
    },
  }
};

export default heatmapChartData;