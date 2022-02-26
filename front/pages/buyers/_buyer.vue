<template>
  <Travaux 
  :done=done 
  :inprogress=inprogress 
  :pieStats=pieStats
  :barOneStats=barOneStats
  :barTwoStats=barTwoStats
  :lineStats=lineStats

  v-on:pie-year-change="fetchPieStats($event)"
  v-on:line-years-change="fetchLineStats($event)"
  v-on:barone-year-change="fetchBarOneStats($event)"
  v-on:bartwo-year-change="fetchBarTwoStats($event)"
  />
</template>

<script>
export default {
  data(){
    return {
        id: this.$route.params.buyer
    }
  },
  mounted(){
    this.$store.dispatch('records',this.id)
    this.$store.dispatch('statasOfBuyer',this.id)
    this.fetchPieStats(new Date().getFullYear())
    this.fetchBarOneStats(new Date().getFullYear())
    this.fetchBarTwoStats(new Date().getFullYear())
    this.fetchLineStats([new Date().getFullYear(), new Date().getFullYear()])
  },
  methods: {
    fetchPieStats(year) {
      this.$store.dispatch('fetchBuyerPieStats', { buyer_id: this.id, year })
    },
    fetchBarOneStats(year) {
      this.$store.dispatch('fetchBuyerBarOneStats', { buyer_id: this.id, year })
    },
    fetchBarTwoStats(year) {
      this.$store.dispatch('fetchBuyerBarTwoStats', { buyer_id: this.id, year })
    },
    fetchLineStats([startYear, endYear]) {
      this.$store.dispatch('fetchBuyerLineStats', { buyer_id: this.id, start_year: startYear, end_year: endYear })
    },
  },
  computed:{
    done(){
      return this.$store.state.listOfRecords
    },
    inprogress(){
      return this.$store.state.recordsInprogress
    },
    pieStats() {
      return this.$store.state.buyerPieStats
    },
    barOneStats() {
      return this.$store.state.buyerBarOneStats
    },
    barTwoStats() {
      return this.$store.state.buyerBarTwoStats
    },
    lineStats() {
      return this.$store.state.buyerLineStats
    }
  }
}
</script>
