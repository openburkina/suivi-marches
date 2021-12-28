<template>
    
    <PieChart :chartData="chartData" />
  
</template> 

<script>
export default {

  data(){
      return {
            chartData:{
                datasets: [{
                    label: 'My First Dataset',
                    data: [65, 59, 80, 81, 56, 55, 40],
                   backgroundColor: ["red","blue","indigo","grey","green","aqua","orange"],
                     hoverOffset: 8
                }]
            }
        }
    }
}
</script>

