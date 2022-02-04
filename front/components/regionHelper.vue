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
          :pieChartLabels="['done', 'in progress']" :pieChartData="[3,4]"
          :lineChartLabels="['2020', '2021', '2022', '2023']" :lineChartData="seriesLine"
          :barChartOneLabels="['Iraq', 'Afghanistan', 'Tunisie', 'Afrique du Sud']" :barChartOneData="[30, 40, 35, 50]"
          :barChartTwoLabels="['Iraq', 'Afghanistan', 'Tunisie', 'Afrique du Sud']" :barChartTwoData="[30, 40, 35, 50]"
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
    }
  },
    data () {
      return {
        tab: null,
        seriesLine: [
          {
            name: 'Sécurité',
            data: [10, 20, 30, 40],
          },
          {
            name: 'Santé',
            data: [15, 25, 35, 50],
          },
          {
            name: 'Éducation',
            data: [9, 7, 13, 20],
          },
          {
            name: 'Agriculture',
            data: [5, 3, 8, 26],
          },
        ],
      }
    },
    mounted(){
    for(this.annee;this.annee<2032;this.annee++){
      this.items.push(this.annee)
    }
  },
}
</script>
