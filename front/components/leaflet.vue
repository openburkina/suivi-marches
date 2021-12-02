<template>
    <div style="height: 80vh ;" class="mt-5">
        <client-only>
            <l-map :zoom=5 :center="[9.548624660911141, 7.804160193482599]" class="map">
            <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
            <l-marker :lat-lng="[8.592724737747833, 16.074241050333463]" @mouseenter="hovering" @mouseleave="notHovering">
               <l-popup >Hahha</l-popup>
            </l-marker>
    
            <l-marker :lat-lng="[9.548624660911141, 7.804160193482599]" @mouseenter="hovering" @mouseleave="notHovering">
                <l-popup>
                    test 2
                </l-popup>
            </l-marker>
            <l-marker :lat-lng="[12.125553758062672, 15.055388119977]" @mouseenter="hovering" @mouseleave="notHovering">
                <l-popup>
                    test 2
                </l-popup>
            </l-marker>
            </l-map>
        </client-only>

    </div>
</template>

<script>
    // import {L} from 'nuxt-leaflet'; 
export default {
    data(){
        return {
           
        }
    },
    mounted() {
  },
  
  methods:{
      hovering(){
        
      },
    notHovering(){
         
      },
  }
}
</script>
<style scoop lang="scss">
.map{
    z-index:0;
}
</style>