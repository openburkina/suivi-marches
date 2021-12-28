<template>
    
    <BarChart :chartData="chartData" />
  
</template> 

<script>
export default {

  data(){
      return {
            chartData:{
                labels: ["jan","fevrier","mars","avril","mai","juin","juillet"],
                 title: {
                        display: false,
                        text: 'Chart.js Pie Chart'
                    },
                datasets: [{
                    label: 'My BarChart',
                    data: [65, 59, 80, 81, 56, 55, 40],
                    backgroundColor: Object.values(["indigo","red","blue","grey","green","aqua","orange"]),
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            }
        }
    }
}
</script>

