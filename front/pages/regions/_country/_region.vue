<template>
  <RegionHelper 
  :done=done 
  :pieStats= pieStats
  :barOneStats= barOneStats
  :barTwoStats= barTwoStats
  :lineStats= lineStats
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
    let country = this.country
    let region = this.region
    this.$store.dispatch('fetchRegionPieStats', { country, region, year: 2015 })
    this.$store.dispatch('fetchRegionBarOneStats', { country, region, year: 2015 })
    this.$store.dispatch('fetchRegionBarTwoStats', { country, region, year: 2015 })
    this.$store.dispatch('fetchRegionLineStats', { country, region, start_year: 2016, end_year: 2021 })
    this.$store.dispatch('oneRegion',{country, region})
  },
}
</script>
