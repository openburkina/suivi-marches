<template>
  <Travaux :done=done :inprogress=inprogress />
</template>

<script>
export default {
   validate({ params }){
       return /^\d+$/.test(params.works)
    },
  data(){
    return {
        id: this.$route.params.works
    }
  },
  mounted(){
    this.$store.dispatch('recordsDone',this.id)
    this.$store.dispatch('recordsInprogress',this.id)
  },
  computed:{
    done(){
      return this.$store.state.recordsDone
    },
    inprogress(){
      return this.$store.state.recordsInprogress
    }
  }
}
</script>
