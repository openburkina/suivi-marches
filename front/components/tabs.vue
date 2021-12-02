<template>
<v-container>
    <p class="display-2 text-center mt-5 font-weight-bold">Explore  <span id="explore"></span></p>
    <p class="text-center">Learn more about where and how UNDP is making a difference around the globe. Search by location, donor <br>country, our focus, signature solution or Sustainable Development Goal.</p>
    <v-tabs class="ml-auto " v-model="tab" grow  slider-size="1" hide-slider>
        <v-tab >
          <v-btn outlined rounded>
            RECIPIENT COUNTRY / TERRITORY / REGION
          </v-btn>
         </v-tab>
        <v-tab>
          <v-btn outlined rounded> DONORS</v-btn>
         
        </v-tab>
        <v-tab>
          <v-btn outlined rounded>our focus</v-btn>
        </v-tab>
        <v-tab>
          <v-btn outlined rounded>
             OUR FOCUSSIGNATURE SOLUTIONS
          </v-btn>
         </v-tab>
        <v-tab>
          <v-btn outlined rounded>
            SDGs
          </v-btn>
          </v-tab>
  </v-tabs>
     <v-tabs-items v-model="tab">
      <v-tab-item>
       
         <Leaflet />
      </v-tab-item>
    <v-tab-item>
        <v-card flat>
          <v-card-text class="display-2">Donors page</v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text class="display-2">Our focus Page {{ $store.state.msg }}</v-card-text>
        </v-card>
      </v-tab-item>

    <v-tab-item >
            <v-card flat>
              <v-card-text class="display-2">focussignature solution page</v-card-text>
            </v-card>
          </v-tab-item>

    <v-tab-item>
        <v-card flat>
          <v-card-text class="display-2">SDGs page</v-card-text>
        </v-card>
      </v-tab-item>

    </v-tabs-items>
</v-container>
</template>
<script>
  import {mapState,mapMutations,mapGetters,mapActions} from 'vuex'
  export default {
    
    data () {
      return {
        tab: null,
       
      }
    },
  }
</script>

<style lang="scss" scoped>
.v-tabs{
  background-color: red ;
}
#explore{
    background-color: #5C6BC0;
    width: 80px;
    height: 8px;
    margin: 0 auto;
    display: block;
    margin-top: 10px;
    margin-bottom: 30px;
}
</style>
