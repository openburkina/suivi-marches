<template>
  <v-app dark>
    <v-container v-if="error.statusCode === 404">
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
        <span class="font-weight-bold mx-5" id="spn">Go Home</span>   
        </v-btn>  
      </div>
    </v-container>
    <h1 v-else>
      {{ otherError }}
    </h1>
   
  </v-app>
</template>

<script>
export default {
  layout: 'error-layout',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      pageNotFound: '404 Not Found',
      otherError: 'An error occurred'
    }
  },
  head () {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    return {
      title
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 20px;
}
#spn{
  font-size: 20px;
}
</style>
