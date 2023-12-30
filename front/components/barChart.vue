<template>
    <v-card
      class="my-5"
      outlined
      tile
      elevation="5"
     >
      <v-card-title class="text-h5" style="word-break: break-word">{{ title }}</v-card-title>
      <v-card-subtitle>
          <v-col cols=12 sm=4>
              <v-text-field
                  v-model="year"
                  label="Année"
                  type="number"
                  v-on:change="$emit('year-change', $event)"
                  />
          </v-col>
      </v-card-subtitle>
      <v-divider></v-divider>
      <div v-if="verif.length==0">
          <P style="height: 300px;text-align: center;color: crimson;">No Data Found</P>
      </div>
      <div v-else>  
      <apexchart 
          type="bar"
          :options="chartOptionsBar"
          :series="seriesBar"
          :height="300">
      </apexchart>
      </div>
      </v-card>
  </template>
  
  <script>
  export default {
      props: ["title", "chartOptionsBar","seriesBar","verif"],
      data() {
          return {
              year : new Date().getFullYear(),
              
          }
      }
  }
  </script>
  