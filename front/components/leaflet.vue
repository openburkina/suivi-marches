<template>
    <div style="height: 80vh ;" class="mt-5">
        <client-only>
            <l-map class="map" :zoom=3 :center=firstDataLocality>
                <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                    <l-marker v-for="d in regionValues" :lat-lng="[d.locality_lat, d.locality_long]" @mouseenter="hovering(d.name)" @mouseleave="notHovering(d.name)" :ref="d.name" :key="d.id">
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
                    </l-marker>
            </l-map>
        </client-only>
    </div>
</template>
<script>

export default {
    props: {
        regionValues: {'data': []}
    },
    data(){
        return {
           open:null
        }
    },
  
  methods:{
    formatValue(amount, currency) {
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
  },
  computed: {
      firstDataLocality() {
          return [this.regionValues[0].locality_lat, this.regionValues[0].locality_long]
      }
  }
}
</script>
<style scoop lang="scss">
.map{
    z-index:0;
}
</style>