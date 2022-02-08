<template>
   <v-card
    class="my-5"
    outlined
    tile
    elevation="5"
    max-width="500">
    <v-card-title class="display-1">Evolution des Montants par secteurs</v-card-title>
    <v-card-subtitle>
        <v-row>
            <v-col cols=12 sm=4>
                <v-text-field
                    v-model="years[0]"
                    :rules="[rules.isLess]"
                    label="Année de début"
                    type="number"
                    v-on:change="handleYearChange"
                    />
            </v-col>
            <v-col cols=12 sm=4>
                <v-text-field
                    v-model="years[1]"
                    :rules="[rules.isGreater]"
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
            years : [new Date().getFullYear(), new Date().getFullYear()],
            rules : {
                isLess : (value) => {
                    if (value <= this.years[1]) return true;
                    return "L'année doit être inférieure ou égale à l'année de fin."
                },
                isGreater : (value) => {
                    if (value >= this.years[0]) return true;
                    return "L'année doit être supérieure ou égale à l'année de fin."
                },
            }
        }
    },
    methods: {
        handleYearChange() {
            if (this.years[0] <= this.years[1]) this.$emit('years-change', this.years);
        }
    }
}
</script>

