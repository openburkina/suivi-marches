<template>
<v-container fluid>
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
          <v-row no-gutters class="mx-3 mt-5">
      <v-col>
        <v-card
          class="my-5"
          max-height="500" max-width="370"
          outlined
          tile
          elevation="5"

        >
         <BarChartContent />

          
        </v-card>
      </v-col>
      <v-col order="12">
        <v-card
          class="my-5"
          max-height="500" max-width="370"
          outlined
          tile
          elevation="5"

        >
          <PieChartContent />
        </v-card>
      </v-col>
      <v-col order="1">
        <v-card
          class="my-5"
          max-height="500" max-width="370"
          outlined
          tile
          elevation="5"
        >
        <LineChartContent />
        </v-card>
      </v-col>
    </v-row>
      </v-tab-item>
    <v-tab-item>
        <v-card flat>
          <v-card-text class="display-2">Donors page</v-card-text>
        </v-card>
      </v-tab-item>
      <v-tab-item>
        <v-card flat>
          <v-card-text class="display-2">Our focus Page</v-card-text>
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
  export default {
    
    data () {
      return {
        tab: null,
       
      }
    },
  }
</script>
