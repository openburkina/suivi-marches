<template>
    <div>
        <v-row>
            <v-col order="6">
                <PieChart 
                :title="pieTitle" 
                :pieOptions="pieChart.options" 
                :pieChartData="pieChart.series" 
                v-on:year-change="pieYearChange"
                />
            </v-col>
            <v-col order="6">
                <LineChart 
                :title="lineTitle" 
                :chartOptionsLine="lineChart.options" 
                :lineSeries="lineChart.series" 
                v-on:years-change="lineYearsChange"
                />
            </v-col>
        </v-row>
        <v-row>
            <v-col order="6">
                <v-col order="6">
                    <BarChart 
                    :title="barOneTitle" 
                    :chartOptionsBar="barChartOne.options" 
                    :seriesBar="barChartOne.series" 
                    v-on:year-change="barOneYearChange"
                    />
                </v-col>
            </v-col>
            <v-col order="6">
                <v-col order="6">
                    <BarChart 
                    :title="barTwoTitle" 
                    :chartOptionsBar="barChartTwo.options" 
                    :seriesBar="barChartTwo.series" 
                    v-on:year-change="barTwoYearChange"
                    />
                </v-col>
            </v-col>
        </v-row>
    </div>
</template>

<script>
export default {
    props : {
        pieTitle: "", pieChartLabels: Array, pieChartData: Array,
        lineTitle: "", lineChartLabels: Array, lineChartData: Array,
        barOneTitle: "", barChartOneLabels: Array, barChartOneData: Array,
        barTwoTitle: "", barChartTwoLabels: Array, barChartTwoData: Array
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
    },
    methods: {
        pieYearChange(value) {
            this.$emit("pie-year-change", value)
        },
        barOneYearChange(value) {
            this.$emit("barone-year-change", value)
        },
        barTwoYearChange(value) {
            this.$emit("bartwo-year-change", value)
        },
        lineYearsChange(value) {
            this.$emit("line-years-change", value)
        },
    }
}
</script>