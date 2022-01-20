<template>
    
    <LineChart :chartData="chartData" />
  
</template> 

<script>
export default {

  data(){
      return {
            chartData:{
                labels: ["jan","fevrier","mars","avril","mai","juin","juillet"],
                datasets: [{
                    label: 'My BarChart',
                    data: [65, 59, 80, 81],
                    backgroundColor: ['#d2d6de', '#a2d6de', '#b2d6de', '#c2d6de'],
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1

                }]
            },
          
        }
    }
}
</script>

