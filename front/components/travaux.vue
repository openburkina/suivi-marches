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
        <TravauxContentDone :title=this.$store.state.particularName :done=done />
      </v-tab-item>
      <v-tab-item class="mx-5">
        <v-container>
        <v-row>
          <v-col order="6">
            <PieChart :pieChartData="label" :pieOptions="statas" />
          </v-col>
          <v-col order="6">
            <LineChart :chartOptionsLine="chartOptionsLine" :lineSeries="seriesLine" />
          </v-col>
        </v-row>
        <v-row>
          <v-col order="6">
            <v-col order="6">
              <BarChart :chartOptionsBar="chartOptionsBar1" :seriesBar="seriesBar1" />
            </v-col>
          </v-col>
          <v-col order="6">
            <v-col order="6">
              <BarChart :chartOptionsBar="chartOptionsBar1" :seriesBar="seriesBar1" />
            </v-col>
          </v-col>
        </v-row>
         </v-container>
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
        label:{
          labels: ['Términé', 'En cours'],
        },
        chartOptionsLine: {
        chart: {
          id: 'vuechart-example',
        },
        xaxis: {
          categories: ['Sécurité', 'Santé', 'Éducation', 'Agriculture'],
        },
      },
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
      chartOptionsBar1: {
        chart: {
          id: 'vuechart-example',
        },
        xaxis: {
          categories: ['Iraq', 'Afghanistan', 'Tunisie', 'Afrique du Sud'],
        },
        colors: '#008FFB',
      },
      seriesBar1: [
        {
          name: 'Pays',
          data: [30, 40, 35, 50],
        },
      ],
      
      }
    },
    computed:{
    recordsDone(){
      return this.$store.state.listOfRecords
    },
    progress(){
      return this.$store.state.listOfRecords
    },
    statas(){
      return [this.recordsDone.length, this.progress.length]
    }
  },
}
</script>
