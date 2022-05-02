<template>
    <div>
        <Caroussel />
        <p class="display-2 text-center font-weight-bold mb-5 mt-5">Maps</p><span id="explore"></span>
       
        <Home
        :pieStats= pieStats
        :barOneStats= barOneStats
        :barTwoStats= barTwoStats
        :lineStats= lineStats
        :activeRegions= regionValues

        v-on:pie-year-change="fetchPieStats($event)"
        v-on:line-years-change="fetchLineStats($event)"
        v-on:barone-year-change="fetchBarOneStats($event)"
        v-on:bartwo-year-change="fetchBarTwoStats($event)"
        />
    </div>
</template>
<script>
export default {
   mounted(){
    this.$store.dispatch('fetchBuyers')
    this.fetchRegionValues()
    this.fetchPieStats(new Date().getFullYear())
    this.fetchBarOneStats(new Date().getFullYear())
    this.fetchBarTwoStats(new Date().getFullYear())
    this.fetchLineStats([new Date().getFullYear(), new Date().getFullYear()])
  },
  methods: {
    fetchPieStats(year) {
      this.$store.dispatch('fetchHomePieStats', { year: year })
    },
    fetchBarOneStats(year) {
      this.$store.dispatch('fetchHomeBarOneStats', { year: year })
    },
    fetchBarTwoStats(year) {
      this.$store.dispatch('fetchHomeBarTwoStats', { year: year })
    },
    fetchLineStats([startYear, endYear]) {
      this.$store.dispatch('fetchHomeLineStats', { start_year: startYear, end_year: endYear })
    },
    fetchRegionValues() {
      console.log("fetching regions values")
      this.$store.dispatch('fetchHomeRegionValues')
    }
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
    regionValues() {
      return this.$store.state.homeRegionValues
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
<style lang="scss" scoped>

#explore{
    background-color: #5C6BC0;
    width: 80px;
    height: 8px;
    margin: 0 auto;
    display: block;
    margin-top: 10px;
}
</style>
