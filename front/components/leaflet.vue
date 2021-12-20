<template>
    <div style="height: 80vh ;" class="mt-5">
        <client-only>
            <l-map :zoom=5 :center="[9.548624660911141, 7.804160193482599]" class="map">
                <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                    <l-marker v-for="d in mock"  :lat-lng=d.lat @mouseenter="hovering(d.name)" @mouseleave="notHovering(d.name)" :ref="d.name" :key="d.id">
                        <l-popup ref="popup">{{ d }}</l-popup>
                    </l-marker>
                 
            </l-map>
        </client-only>
    </div>
</template>
<script>

export default {
    data(){
        return {
           open:null,
           mock:[
               {
                   id:0,
                   msg:"hello from 0",
                   name:'tchad',
                   lat:[8.592724737747833, 16.074241050333463]

               },
                {
                   id:1,
                   msg:"hello from 1",
                   name:'adams',
                   lat:[9.548624660911141, 7.804160193482599]

               },
                 {
                   id:2,
                   msg:"hello from 2",
                   name:'ndja',
                   lat:[12.125553758062672, 15.055388119977]

               },
                {
                   id:3,
                   msg:"hello from 3",
                   name:'adam',
                   lat:[12.125553758062672, 15.055388119977]

               },
                {
                   id:4,
                   msg:"hello from 4",
                   name:'nig',
                   lat:[11.125553758062672, 12.055388119977]

               }  
           ]
        }
    },
  
  methods:{
  
    hovering(name){
        console.log(this.$refs.marker)
        console.log(this.$refs[name][0])
        this.$nextTick(() => {
            this.$refs[name][0].mapObject.openPopup()

        }) 
      },
    notHovering(name){
        console.log(name)
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