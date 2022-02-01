<template>
  <RegionHelper :done=region />
</template>

<script>
export default {
   validate({ params }){
       return /^\d+$/.test(params.regions)
    },
  data(){
    return {
        id: this.$route.params.regions
    }
  },
  mounted(){
    this.$store.dispatch('oneRegion',this.id)
  },
  computed:{
    region(){
      return this.$store.state.listRegions
    },
  }
}
</script>
