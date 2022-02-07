<template>
    <div>
        <Caroussel />
        <p class="display-2 text-center font-weight-bold mb-5 mt-5">Explore  <span id="explore"></span></p>
       
        <Tabs 
        :pieStats= pieStats
        :barOneStats= barOneStats
        :barTwoStats= barTwoStats
        :lineStats= lineStats

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
    this.fetchPieStats(new Date().getFullYear())
    this.fetchBarOneStats(new Date().getFullYear())
    this.fetchBarTwoStats(new Date().getFullYear())
    this.fetchLineStats([new Date().getFullYear(), new Date().getFullYear()])
  },
  methods: {
    fetchPieStats(year) {
      console.log("fetching pie...")
      this.$store.dispatch('fetchHomePieStats', { year: year })
    },
    fetchBarOneStats(year) {
      console.log("fetching bar one...")
      this.$store.dispatch('fetchHomeBarOneStats', { year: year })
    },
    fetchBarTwoStats(year) {
      console.log("fetching bar two...")
      this.$store.dispatch('fetchHomeBarTwoStats', { year: year })
    },
    fetchLineStats([startYear, endYear]) {
      console.log("fetching line...")
      this.$store.dispatch('fetchHomeLineStats', { start_year: startYear, end_year: endYear })
    },
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
