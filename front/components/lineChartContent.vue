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
                    label: 'My LineChart',
                    data: [65, 59, 80, 81, 56, 55, 40],
                   
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1,
                    backgroundColor: Object.values(['rgb(75, 192, 192)']),

                }]
            },
          
        }
    }
}
</script>

