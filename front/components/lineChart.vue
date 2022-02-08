<template>
   <v-card
    class="my-5"
    outlined
    tile
    elevation="5"
    max-width="500">
    <v-card-title class="display-1" style="word-break: break-word">{{ title }}</v-card-title>
    <v-card-subtitle>
        <v-row>
            <v-col cols=12 sm=4>
                <v-text-field
                    v-model="years[0]"
                    label="Année de début"
                    type="number"
                    v-on:change="handleYearChange"
                    />
            </v-col>
            <v-col cols=12 sm=4>
                <v-text-field
                    v-model="years[1]"
                    label="Année de fin"
                    type="number"
                    v-on:change="handleYearChange"
                    />
            </v-col>
        </v-row>
    </v-card-subtitle>
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
    props: ["title", "chartOptionsLine","lineSeries"],
    data() {
        return {
            years : [new Date().getFullYear(), new Date().getFullYear()]
        }
    },
    methods: {
        handleYearChange(val) {
            this.$emit('years-change', this.years)
        }
    }
}
</script>

