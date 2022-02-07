<template>
  <v-card
    class="my-5"
    max-width="500"
    outlined
    tile
    elevation="5">
    <v-card-title class="display-1">
        Montant par secteur
    </v-card-title>
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
    props: [
        "title",
        "pieChartData",
        "pieOptions"
    ],
    data() {
        return {
            year : new Date().getFullYear()
        }
    }
}
</script>
