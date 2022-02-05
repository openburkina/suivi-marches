<template>
    <v-container>
        <v-row>
            <v-col order="6">
                <PieChart :pieOptions="pieChart.options" :pieChartData="pieChart.series" />
            </v-col>
            <v-col order="6">
                <LineChart :chartOptionsLine="lineChart.options" :lineSeries="lineChart.series" />
            </v-col>
        </v-row>
        <v-row>
            <v-col order="6">
                <v-col order="6">
                    <BarChart :chartOptionsBar="barChartOne.options" :seriesBar="barChartOne.series" />
                </v-col>
            </v-col>
            <v-col order="6">
                <v-col order="6">
                    <BarChart :chartOptionsBar="barChartTwo.options" :seriesBar="barChartTwo.series" />
                </v-col>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
export default {
    props : {
        pieChartLabels: Array, pieChartData: Array,
        lineChartLabels: Array, lineChartData: Array,
        barChartOneLabels: Array, barChartOneData: Array,
        barChartTwoLabels: Array, barChartTwoData: Array
    },
    computed: {
        pieChart() { 
            return {
                options : {
                    labels: this.pieChartLabels
                },
                series : this.pieChartData
            }
        },
        lineChart() {
            return {
                options : {
                    chart : {
                        id : 'vuechart-example',
                    },
                    xaxis : {
                        categories: this.lineChartLabels
                    },
                },
                series : this.lineChartData
            }
        },
        barChartOne() {
            return {
                options : {
                    chart: {
                        id: 'vuechart-example',
                    },
                    xaxis: {
                        categories: this.barChartOneLabels,
                    },
                    colors: '#008FFB',
                },
                series : [{
                    name: 'Montant',
                    data: this.barChartOneData
                }]
            }
        },
        barChartTwo() {
            return {
                options : {
                    chart: {
                        id: 'vuechart-example',
                    },
                    xaxis: {
                        categories: this.barChartTwoLabels,
                    },
                    colors: '#008FFB',
                },
                series : [{
                    name: 'Montant',
                    data: this.barChartTwoData,
                }]
            }
        }
    }
}
</script>