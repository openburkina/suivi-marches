<template>
  <v-card
    class="my-5"
    outlined
    tile
    elevation="5"
    max-width="500">
    <v-card-title class="text-h5">Montant par r&eacute;gions</v-card-title>
    <v-card-subtitle>Montant des projets par r&eacute;gions</v-card-subtitle>
    <v-divider></v-divider>
    <apexchart
        type="bar"
        :options="chartOptionsBar"
        :series="seriesBar"
        :max-width="500"
        :height="300">
    </apexchart>
    </v-card>
</template>

<script>
export default {
    props: ["chartOptionsBar","seriesBar"],
}
</script>
