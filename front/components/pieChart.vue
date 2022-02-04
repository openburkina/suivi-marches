<template>
  <v-card
    class="my-5"
    max-width="500"
    outlined
    tile
    elevation="5">
    <v-card-title class="display-1">Statut des projets</v-card-title>
        <v-divider></v-divider>
        <apexchart
            type="donut"
            :options="pieOptions"
            :series="pieChartData"
            :max-width="500"
            :height="300">
        </apexchart> 
    </v-card>
</template>

<script>
export default {
    props: ["pieChartData","pieOptions"],

}
</script>
