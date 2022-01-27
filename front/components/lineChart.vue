<template>
   <v-card
    class="my-5"
    outlined
    tile
    elevation="5"
    max-width="500">
    <v-card-title class="display-1">Montant par secteurs</v-card-title>
    <v-divider></v-divider>
        <apexchart
            type="line"
            :options="chartOptionsLine"
            :series="lineSeries"
            :max-width="500"
            :height="300">
        </apexchart>
    </v-card>
</template>

<script>
export default {
    props: ["chartOptionsLine","lineSeries"],

}
</script>

