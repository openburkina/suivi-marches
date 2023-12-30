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
        <ChartList 
          :pieTitle="pieTitle" :pieChartLabels="pieStats.labels" :pieChartData="pieStats.data" v-on:pie-year-change="$emit('pie-year-change', $event)"
          :lineTitle="lineTitle" :lineChartLabels="lineStats.labels" :lineChartData="lineStats.data" v-on:line-years-change="$emit('line-years-change', $event)"
          :barOneTitle="barOneTitle" :barChartOneLabels="barOneStats.labels" :barChartOneData="barOneStats.data" v-on:barone-year-change="$emit('barone-year-change', $event)"
          :barTwoTitle="barTwoTitle" :barChartTwoLabels="barTwoStats.labels" :barChartTwoData="barTwoStats.data" v-on:bartwo-year-change="$emit('bartwo-year-change', $event)"
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
      tab: null,
      pieTitle: "Statut annuel des travaux",
      lineTitle: "Evolution des montants par secteur",
      barOneTitle: "Montant annuel des travaux par région",
      barTwoTitle: "Montant annuel des travaux par secteur",
    }
  },
  computed: {
    statas() {
      console.log(this.$store.state.statasList)
      return this.$store.state.statasList
    }
  }
}
</script>
