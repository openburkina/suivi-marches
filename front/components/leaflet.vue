<template>
    <div style="height: 80vh ;" class="mt-5">
        <client-only>
            <l-map class="map" :zoom=3 :center=centerPoint>
                <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                <l-polygon v-for="d in regions" :lat-lngs="d.boundary.coordinates" :fillColor="getColor(d.id)" :fillOpacity="1" @mouseenter="hovering(d.region)" @mouseleave="notHovering(d.region)" :ref="d.region" :key="d.id">
                        <l-popup ref="popup">
                           <p>{{ d.region }}</p>
                            <v-card >
                                <template>
                                    <v-simple-table>
                                        <template v-slot:default>
                                        <tbody>
                                         <!-- <tr> <td>Montant</td> <td>{{ formatValue(d.value, d.currency) }}</td></tr> -->
                                        </tbody>
                                        </template>
                                    </v-simple-table>
                                    </template>
                            </v-card>
                        </l-popup>
                </l-polygon>
                    <!-- <l-marker v-for="d in regionValues" :lat-lng="[d.locality_lat, d.locality_long]" @mouseenter="hovering(d.name)" @mouseleave="notHovering(d.name)" :ref="d.name" :key="d.id">
                        <l-popup ref="popup">
                           <p>{{ d.name }}</p>
                            <v-card >
                                <template>
                                    <v-simple-table>
                                        <template v-slot:default>
                                        <tbody>
                                         <tr> <td>Montant</td> <td>{{ formatValue(d.value, d.currency) }}</td></tr>
                                        </tbody>
                                        </template>
                                    </v-simple-table>
                                    </template>
                            </v-card>
                        </l-popup>
                    </l-marker> -->
            </l-map>
        </client-only>
    </div>
</template>
<script>
import * as regions from '../static/data/regions_cached.json';
export default {
    props: {
        activeRegions: {'data': []}
    },
    data(){
        return {
            open:null,
            centerPoint : [-3.993859, 29.371619],
            regions: regions.data
        }
    },
    methods:{
        getColor(id) {
            try {
                let region = this.activeRegions.find((region) => region.region_id == id);
                if (region != undefined){
                    if (region.value > 0) return "#7DDE99"
                    if (region.value > 100000) return "#DDCF6C"
                    if (region.value > 1000000) return "#2AA24C"
                }
                return "#FFF"
            } catch (e) {
                console.log(this.activeRegions)
                console.log(e)
                return "#FFF"
            }
        },
        formatValue(amount, currency) {
            if (amount==null && currency==null){
                amount = 0
                currency = "$"
            }
            return (
                amount
                .toFixed(2) // always two decimal digits
                .replace('.', ',') // replace decimal point character with ,
                .replace(/(\d)(?=(\d{3})+(?!\d))/g, '$1.') + ' ' + currency
            ) 
        },
        hovering(name){
            this.$nextTick(() => {
                this.$refs[name][0].mapObject.openPopup()

            }) 
        },
        notHovering(name){
            this.$nextTick(() => {
                this.$refs[name][0].mapObject.closePopup()
            }) 
        },
    }
}
</script>
<style scoop lang="scss">
.map{
    z-index:0;
}
</style>