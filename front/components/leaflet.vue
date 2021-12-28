<template>
    <div style="height: 80vh ;" class="mt-5">
        <client-only>
            <l-map :zoom=5 :center="[9.548624660911141, 7.804160193482599]" class="map">
                <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
                    <l-marker v-for="d in mock"  :lat-lng=d.lat @mouseenter="hovering(d.name)" @mouseleave="notHovering(d.name)" :ref="d.name" :key="d.id">
                        <l-popup ref="popup">
                           <p class="display-1">{{d.dra}}</p>
                            <v-card >
                                <template>
                                    <v-simple-table>
                                        
                                        <template v-slot:default>
                                        <tbody>
                                         <tr> <td>Projet</td> <td> {{ d.projet }}</td></tr>
                                         <tr> <td>Budget</td> <td> {{ d.budget }}</td></tr>
                                         <tr> <td>Expense</td> <td> {{ d.expense }}</td></tr>
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
    data(){
        return {
           open:null,
           mock:[
               {
                   id:0,
                   name:'tchad',
                   projet:"2",
                   dra:"🇹🇩",
                   budget:"$45M",
                   expense:"100XAF",
                   lat:[8.592724737747833, 16.074241050333463]

               },
                {
                   id:1,
                   projet:"45",
                   budget:"$45M",
                   name:'adams',
                   dra:"🇳🇬",
                    expense:"100XAF",
                   lat:[9.548624660911141, 7.804160193482599]

               },
                 {
                   id:2,
                   projet:"12",
                   budget:"$45M",
                   name:'ndja',
                    dra:"🇹🇩",
                     expense:"100XAF",
                   lat:[12.125553758062672, 15.055388119977]

               },
                {
                   id:3,
                   projet:"75",
                   budget:"$4.3M",
                   name:'adam',
                    dra:"🇹🇩",
                   lat:[12.125553758062672, 15.055388119977]

               },
                {
                   id:4,
                   projet:"55",
                   budget:"$5M",
                   name:'nig',
                   dra:"🇳🇬",
                    expense:"100XAF",
                   lat:[11.125553758062672, 12.055388119977]

               },
                 {
                   id:5,
                   projet:"54",
                   budget:"$4M",
                   name:'nigs',
                  dra:"🇧🇫",
                   expense:"100XAF",
                   lat:[12.2383,1.5616]

               }  
           ]
        }
    },
  
  methods:{
  
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