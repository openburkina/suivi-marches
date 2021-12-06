<template>
  <v-btn
        left="true"
        dark
        color="indigo"
        :to="route"
        >
        {{ title }}
      </v-btn>
</template>

<script>

export default {
    props:['title',"route"]
}
</script>
