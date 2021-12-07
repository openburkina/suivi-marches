<template>
  <div>
     <v-tabs v-model="tab" centered slider-size="1" hide-slider class="mb-5" active-class="active">
        <v-tab
        >
          <v-btn outlined rounded
          color="success"
          >
            <v-icon left>
              mdi-check-all
            </v-icon>
            Travaux terminé
          </v-btn>
         </v-tab>
        <v-tab>
          <v-btn outlined rounded color="indigo lighten-1"> 
            <v-icon left>
              mdi-progress-check
            </v-icon>
            Travaux en cours
          </v-btn>
        </v-tab>
    </v-tabs>
     <v-tabs-items v-model="tab">
      <v-tab-item>
        <TravauxContentDone title='Travaux terminés' :done=done />
      </v-tab-item>
    <v-tab-item>
        <TravauxContentInprogress title='Travaux en cours' :inprogress=inprogress />
      </v-tab-item>
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
    }
  },
    data () {
      return {
        tab: null
      }
    }
}
</script>
