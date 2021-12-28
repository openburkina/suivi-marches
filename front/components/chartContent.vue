<template>
    <div>
        <Chart :chartData="chartData" />
    </div>
</template>

<script>
export default {

  data(){
      return {
          chartData:{
              label: ["ja","d","de","der"],
              datasets:{
                  data:[100,34,120,200]
              }
          }
      }
  }

}
</script>
