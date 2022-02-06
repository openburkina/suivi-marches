<template>
  <div>
     <v-tabs v-model="tab" centered slider-size="1" hide-slider class="mb-5 mt-16" active-class="active">
        <v-tab
        >
          <v-btn outlined rounded
          color="success"
          >
            <v-icon left>
              mdi-clipboard-list-outline
            </v-icon>
            Listes
          </v-btn>
         </v-tab>
        <v-tab>
          <v-btn outlined rounded color="success"> 
            <v-icon left>
              mdi-chart-bar
            </v-icon>
            Statistiques
          </v-btn>
        </v-tab>
    </v-tabs>
     <v-tabs-items v-model="tab">
      <v-tab-item class="mx-5 mt-16 mb-16 elevation-4">
        <SingleRegion :title=this.$store.state.regionName :done=done />
      </v-tab-item>
      <v-tab-item class="mx-5">
        <ChartList 
          :pieChartLabels="pieStats.labels" :pieChartData="pieStats.data"
          :lineChartLabels="lineStats.labels" :lineChartData="lineStats.data"
          :barChartOneLabels="barOneStats.labels" :barChartOneData="barOneStats.data"
          :barChartTwoLabels="barTwoStats.labels" :barChartTwoData="barTwoStats.data"
        />
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

 
<script>
export default {
   props: {
    done: {
        type: []
    },
    inprogress: {
        type: []
    },
    pieStats: {'labels': [], 'data': []},
    barOneStats: {'labels': [], 'data': []},
    barTwoStats: {'labels': [], 'data': []},
    lineStats: {'labels': [], 'data': []},
  },
    data () {
      return {
        tab: null
      }
    },
    mounted(){
    for(this.annee;this.annee<2032;this.annee++){
      this.items.push(this.annee)
    }
  },
}
</script>
