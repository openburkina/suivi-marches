<template>
<v-container fluid>
    <p class="text-center">Learn more about where and how UNDP is making a difference around the globe. Search by location, donor <br>country, our focus, signature solution or Sustainable Development Goal.</p>
    <v-tabs class="ml-auto " v-model="tab" grow  slider-size="1" hide-slider>
        <v-tab >
          <v-btn outlined rounded>
            RECIPIENT COUNTRY / TERRITORY / REGION
          </v-btn>
         </v-tab>
        <v-tab>
          <v-btn outlined rounded> DONORS</v-btn>
        </v-tab>
        <v-tab>
          <v-btn outlined rounded>our focus</v-btn>
        </v-tab>
        <v-tab>
          <v-btn outlined rounded>
             OUR FOCUSSIGNATURE SOLUTIONS
          </v-btn>
         </v-tab>
        <v-tab>
          <v-btn outlined rounded>
            SDGs
          </v-btn>
          </v-tab>
  </v-tabs>
  
     <v-tabs-items v-model="tab">
      <v-tab-item>
       <v-container>

         <Leaflet :regionValues=regionValues  />
       </v-container>
       <v-container>
        <ChartList 
          :pieTitle="pieTitle" :pieChartLabels="pieStats.labels" :pieChartData="pieStats.data" v-on:pie-year-change="$emit('pie-year-change', $event)"
          :lineTitle="lineTitle" :lineChartLabels="lineStats.labels" :lineChartData="lineStats.data" v-on:line-years-change="$emit('line-years-change', $event)"
          :barOneTitle="barOneTitle" :barChartOneLabels="barOneStats.labels" :barChartOneData="barOneStats.data" v-on:barone-year-change="$emit('barone-year-change', $event)"
          :barTwoTitle="barTwoTitle" :barChartTwoLabels="barTwoStats.labels" :barChartTwoData="barTwoStats.data" v-on:bartwo-year-change="$emit('bartwo-year-change', $event)"
        />
        </v-container>
      </v-tab-item>
    <v-tab-item>
        <v-card flat>
          <v-card-text class="display-2">Donors page</v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text class="display-2">Our focus Page</v-card-text>
        </v-card>
      </v-tab-item>

    <v-tab-item >
            <v-card flat>
              <v-card-text class="display-2">focussignature solution page</v-card-text>
            </v-card>
          </v-tab-item>

    <v-tab-item>
        <v-card flat>
          <v-card-text class="display-2">SDGs page</v-card-text>
        </v-card>
      </v-tab-item>

    </v-tabs-items>
</v-container>
</template>
<script>
  export default {
    props: {
      pieStats: {'labels': [], 'data': []},
      barOneStats: {'labels': [], 'data': []},
      barTwoStats: {'labels': [], 'data': []},
      lineStats: {'labels': [], 'data': []},
      regionValues: {'data': []}
    },
    data () {
      return {
        tab: null,
        widthChart: 370,
        pieTitle: "Statut annuel des travaux",
        lineTitle: "Evolution des montants par secteur",
        barOneTitle: "Montant annuel des travaux par région",
        barTwoTitle: "Montant annuel des travaux par secteur",
      }
    },
  
  }
</script>
