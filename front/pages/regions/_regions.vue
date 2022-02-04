<template>
  <RegionHelper :done=done />
</template>

<script>
export default {
   validate({ params }){
       return /^\d+$/.test(params.regions)
      //  return params
    },
  data(){
    return {
      id:this.$route.params.regions
    }
  },
  computed:{
    done(){
      return this.$store.state.listRegions
    },
  },
  mounted(){
    
    this.$store.dispatch('oneRegion',region)
  },
}
</script>
