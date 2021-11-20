<template>
    <v-parallax
        height="810"
        class="mt-5"
        :src="require('~/assets/img/404.jpg')"
      >

       <v-btn
          fixed
          bottom
          to="/"
          >
            <v-icon left>mdi-arrow-left</v-icon> <span class="font-weight-bold">Go Home</span> 
      </v-btn>
    </v-parallax>

</template>
<script>
export default {
    layout:"error"
}
</script>


<style scoped>
 .v-btn{
   color:#458DF3;
 }
</style>