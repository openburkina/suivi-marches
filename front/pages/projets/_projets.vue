<template>
  <Travaux :done=done :inprogress=inprogress />
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
    // this.$store.dispatch('recordsInprogress',this.id)
  },
  computed:{
    done(){
      return this.$store.state.listOfRecords
    },
    inprogress(){
      return this.$store.state.recordsInprogress
    }
  }
}
</script>
