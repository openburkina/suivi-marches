<template>
  <Works 
  :done=done
  />
</template>

<script>
export default {
   validate({ params }){
       //return /^\d+$/.test(params.regions)
       return params
    },
  data(){
    return {
        country: this.$route.params.country,
        region: this.$route.params.region
    }
  },
  computed:{
    done(){
      return this.$store.state.listRegions
    },
    pieStats() {
      return this.$store.state.regionPieStats
    },
    barOneStats() {
      return this.$store.state.regionBarOneStats
    },
    barTwoStats() {
      return this.$store.state.regionBarTwoStats
    },
    lineStats() {
      return this.$store.state.regionLineStats
    }
  },
  mounted(){
    this.fetchPieStats(new Date().getFullYear())
    this.fetchBarOneStats(new Date().getFullYear())
    this.fetchBarTwoStats(new Date().getFullYear())
    this.fetchLineStats([new Date().getFullYear(), new Date().getFullYear()])
    this.$store.dispatch('oneRegion',{country: this.country,region: this.region})
  },
  methods: {
    fetchPieStats(year) {
      this.$store.dispatch('fetchRegionPieStats', { country: this.country,region: this.region, year })
    },
    fetchBarOneStats(year) {
      this.$store.dispatch('fetchRegionBarOneStats', { country: this.country,region: this.region, year })
    },
    fetchBarTwoStats(year) {
      this.$store.dispatch('fetchRegionBarTwoStats', { country: this.country,region: this.region, year })
    },
    fetchLineStats([startYear, endYear]) {
      this.$store.dispatch('fetchRegionLineStats', { country: this.country,region: this.region, start_year: startYear, end_year: endYear })
    },
  },
}
</script>
