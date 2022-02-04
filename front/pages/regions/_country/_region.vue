<template>
  <RegionHelper :done=done />
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
  },
  mounted(){
    let country = this.country
    let region = this.region
    this.$store.dispatch('oneRegion',{country, region})
  },
}
</script>
