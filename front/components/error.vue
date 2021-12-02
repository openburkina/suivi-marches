<template>
  <div align="center" class="mb-5">
      <v-img 
        max-width="500"
        :src="require('~/assets/img/adam.png')"
      />
      <v-btn
        color="indigo"
        dark
        rounded
        large
        class="mt-3"
        to="/"
        >
      <v-icon left large class="mx-5">mdi-arrow-left</v-icon>
        <span class="font-weight-bold mx-5" id="spn">Get me out of there !</span>   
      </v-btn>  
  </div>
</template>

<script>
export default {
layout:'error'
}
</script>
<style scoop>
#spn{
  font-size: 20px;
}
</style>