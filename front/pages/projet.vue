<template>
  <DoneProject title='Travaux terminés' />
</template>

<script>
export default {

  data () {
      return {
        tab: null,
      }
  },
  mounted(){
    this.Fetchbuyers()
    
  },
 
  computed:{
    allBuyers(){
      return this.$store.state.buyers
    }
  },
  methods:{
   Fetchbuyers(){
     console.log("hello",this.$store.state.buyers)
      return this.$store.dispatch('fetchBuyers')
    },
  
  }
}
</script>

