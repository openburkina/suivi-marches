<template>
  <Travaux />
</template>

<script>
export default {

  mounted(){
     this.$store.dispatch('fetchBuyers')
  },
 
  computed:{
    text(){
      return this.$store.state.list
    }
  },
  methods:{
  
  }
}
</script>

