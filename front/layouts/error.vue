<template>
  <v-app dark>
    <v-container v-if="error.statusCode === 404">
      <Error />
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

</style>
