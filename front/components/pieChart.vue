<template>
  <v-card
    class="my-5"
    outlined
    tile
    elevation="5">
    <v-card-title class="text-h5" style="word-break: break-word">
        {{ title }}
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
    <div v-if="pieChartData[0]==0 && pieChartData[1]==0 && pieChartData[2]==0 && pieChartData[3]==0 && pieChartData[4]==0 && pieChartData[5]==0">
        <P style="height: 300px;text-align: center;color: crimson;">No Data Found</P>
    </div>    
    <div v-else>
        <apexchart
        type="donut"
        :options="pieOptions"
        :series="pieChartData"
        :height="300"
        >   
        </apexchart>
    </div>
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
