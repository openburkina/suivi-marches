<template>
  <v-btn
        left="true"
        dark
        :color="color"
        :to="route"
        >
        {{ title }}
      </v-btn>
</template>

<script>

export default {
    props:["title","route","color"]
}
</script>
