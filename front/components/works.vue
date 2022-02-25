<template>
  <div>
     <v-tabs v-model="tab" centered slider-size="1" hide-slider class="mb-5 mt-16" active-class="active">
        <v-tab
        >
          <v-btn outlined rounded
          color="success"
          >
            <v-icon left>
              mdi-clipboard-list-outline
            </v-icon>
            Détails
          </v-btn>
         </v-tab>
        <v-tab>
          <v-btn outlined rounded color="success"> 
            <v-icon left>
              mdi-chart-bar
            </v-icon>
            Spécification
          </v-btn>
        </v-tab>
                <v-tab>
          <v-btn outlined rounded color="success"> 
            <v-icon left>
              mdi-chart-bar
            </v-icon>
            Décaissement
          </v-btn>
        </v-tab>
                <v-tab>
          <v-btn outlined rounded color="success"> 
            <v-icon left>
              mdi-chart-bar
            </v-icon>
            Timeline
          </v-btn>
        </v-tab>
    </v-tabs>
     <v-tabs-items v-model="tab">
    </v-tabs-items>
  </div>
</template>

<script>
export default {
  props: {
    done: {
      type: []
    },
    inprogress: {
        type: []
    },
  
  },
  data () {
    return {
      tab: null,
    
    }
  },
  computed: {
    statas() {
      console.log(this.$store.state.statasList)
      return this.$store.state.statasList
    }
  }
}
</script>
