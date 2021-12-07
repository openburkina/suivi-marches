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
        slug: this.$route.params
    }
  },
  mounted(){
    this.$store.dispatch('recordsDone',1)
    this.$store.dispatch('recordsInprogress',1)
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
