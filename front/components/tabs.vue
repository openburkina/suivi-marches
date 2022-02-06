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
         <ChartList 
          :pieChartLabels="pieStats.labels" :pieChartData="pieStats.data"
          :lineChartLabels="lineStats.labels" :lineChartData="lineStats.data"
          :barChartOneLabels="barOneStats.labels" :barChartOneData="barOneStats.data"
          :barChartTwoLabels="barTwoStats.labels" :barChartTwoData="barTwoStats.data"
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
    
  data () {
    return {
      tab: null,
      widthChart: 370,
    }
  },

  mounted(){
    this.$store.dispatch('fetchBuyers')
    this.$store.dispatch('fetchHomePieStats', { year: 2015 })
    this.$store.dispatch('fetchHomeBarOneStats', { year: 2015 })
    this.$store.dispatch('fetchHomeBarTwoStats', { year: 2015 })
    this.$store.dispatch('fetchHomeLineStats', { start_year: 2016, end_year: 2021 })
  },
 
  computed: {
    pieStats() {
      return this.$store.state.homePieStats
    },
    barOneStats() {
      return this.$store.state.homeBarOneStats
    },
    barTwoStats() {
      return this.$store.state.homeBarTwoStats
    },
    lineStats() {
      return this.$store.state.homeLineStats
    },
    done(){
      return this.$store.state.recordsDone.length
    },
    pregress(){
      return this.$store.state.recordsInprogress.length
    }
  },
  }
</script>
