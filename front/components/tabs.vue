<template>
<v-container>
    <p class="display-2 text-center mt-5 font-weight-bold">Explore</p>
    <p class="text-center">Learn more about where and how UNDP is making a difference around the globe. Search by location, donor <br>country, our focus, signature solution or Sustainable Development Goal.</p>
    <v-tabs class="ml-auto" v-model="tab" grow>
        <v-tab outlined>RECIPIENT COUNTRY / TERRITORY / REGION</v-tab>
        <v-tab>DONORS</v-tab>
        <v-tab>OUR FOCUSSIGNATURE SOLUTIONS</v-tab>
        <v-tab>SDGs</v-tab>
  </v-tabs>
     <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="item in items"
        :key="item"
      >
        <v-card flat>
          <v-card-text v-text="text"></v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
</v-container>
</template>
<script>
  export default {
    data () {
      return {
        tab: null,
        items: [
          'web', 'shopping', 'videos', 'images', 'news',
        ],
        text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
      }
    },
  }
</script>