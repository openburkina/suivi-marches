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

         <Leaflet />
       </v-container>
       <v-container>
      <v-row no-gutters class="mx-3 mt-5">
      <v-col order="6">
        <PieChart :pieChartData="chartOptionsD" :pieOptions="seriesD" />
      </v-col>
      <v-col order="6">
       <LineChart :chartOptionsLine="chartOptionsLine" :lineSeries="seriesLine" />
      </v-col>
    </v-row>


    <v-row no-gutters class="mx-3 mt-5">
       <v-col order="6">
         <BarChart :chartOptionsBar="chartOptionsBar1" :seriesBar="seriesBar1" />
       </v-col>
      <v-col order="6">
         <BarChart :chartOptionsBar="chartOptionsBar2" :seriesBar="seriesBar2" />
        </v-col>
    </v-row>
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
    
    data () {
      return {
        tab: null,
         widthChart: 370,
      //
      // BAR1 DATA
      //
      chartOptionsBar2: {
        chart: {
          id: 'vuechart-example',
        },
        xaxis: {
          categories: ['Sécurité', 'Santé', 'Éducation', 'Agriculture'],
        },
        colors: '#00E396',
      },
      seriesBar2: [
        {
          name: 'Secteurs',
          data: [30, 40, 35, 50],
        },
      ],
      //
      // BAR1 DATA
      //
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
      //
      // LINE DATA
      //
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
      //
      // DONUT DATA
      //
      chartOptionsD: {
        labels: ['Términé', 'En cours'],
      },
      seriesD: [34, 66],
      //
      // CAROUSEL DATA
      }
    },
  mounted(){
    this.$store.dispatch('fetchBuyers')
  },
 
  computed:{
    buyers(){
      return this.$store.state.list
    }
  },
  }
</script>
