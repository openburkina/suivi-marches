<template>
  <Travaux 
  :done=done 
  :inprogress=inprogress 
  :pieStats=pieStats
  :barOneStats=barOneStats
  :barTwoStats=barTwoStats
  :lineStats=lineStats
  />
</template>

<script>
export default {
   validate({ params }){
       return /^\d+$/.test(params.projets)
    },
  data(){
    return {
        id: this.$route.params.projets
    }
  },
  mounted(){
    this.$store.dispatch('records',this.id)
    this.$store.dispatch('statasOfBuyer',this.id)
    this.$store.dispatch('fetchBuyerPieStats', { buyer_id: this.id, year: 2015 })
    this.$store.dispatch('fetchBuyerBarOneStats', { buyer_id: this.id, year: 2015 })
    this.$store.dispatch('fetchBuyerBarTwoStats', { buyer_id: this.id, year: 2015 })
    this.$store.dispatch('fetchBuyerLineStats', { buyer_id: this.id, start_year: 2016, end_year: 2021 })
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
