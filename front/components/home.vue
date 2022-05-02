<template>
    <v-container>
        <Leaflet :activeRegions=activeRegions :colorIntervals=colorIntervals  />
        <ChartList 
            :pieTitle="pieTitle" :pieChartLabels="pieStats.labels" :pieChartData="pieStats.data" v-on:pie-year-change="$emit('pie-year-change', $event)"
            :lineTitle="lineTitle" :lineChartLabels="lineStats.labels" :lineChartData="lineStats.data" v-on:line-years-change="$emit('line-years-change', $event)"
            :barOneTitle="barOneTitle" :barChartOneLabels="barOneStats.labels" :barChartOneData="barOneStats.data" v-on:barone-year-change="$emit('barone-year-change', $event)"
            :barTwoTitle="barTwoTitle" :barChartTwoLabels="barTwoStats.labels" :barChartTwoData="barTwoStats.data" v-on:bartwo-year-change="$emit('bartwo-year-change', $event)"
        />
    </v-container>
</template>
<script>
  export default {
    props: {
      pieStats: {'labels': [], 'data': []},
      barOneStats: {'labels': [], 'data': []},
      barTwoStats: {'labels': [], 'data': []},
      lineStats: {'labels': [], 'data': []},
      activeRegions: {'data': []}
    },
    data () {
      return {
        tab: null,
        widthChart: 370,
        pieTitle: "Statut annuel des travaux",
        lineTitle: "Evolution des montants par secteur",
        barOneTitle: "Montant annuel des travaux par région",
        barTwoTitle: "Montant annuel des travaux par secteur",
        colorIntervals: [
                {
                    "key": 0,
                    "value": "0",
                    "color": "#FFF"
                },
                {
                    "key": 1,
                    "value": "< 100.000",
                    "color": "#D72638"
                },
                {
                    "key": 2,
                    "value": "< 1.000.000",
                    "color": "#FFD97D"
                },
                {
                    "key": 3,
                    "value": "> 1.000.000",
                    "color": "#60D394"
                },
            ]
      }
    },
  
  }
</script>
