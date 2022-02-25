<template>
  <v-card>
    <v-card-title>
      {{title}}
       <v-combobox
          v-model="select"
          :items="items"
          label="Choisir l'intervalle des années"
          multiple
          chips
          counter="2"
          @change="onChange"
          auto-select-first
        ></v-combobox>
      <v-spacer></v-spacer>
      <v-text-field
        v-model="search"
        solo
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
        rounded
        
      ></v-text-field>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items=done
      :search="search"
      :items-per-page=5
      :options=
      "{sortBy: []}"
      :footer-props="{
        'items-per-page-text':'Liste de travaux'
      }">
   
    </v-data-table>
  </v-card>
</template>

<script>
export default {
   props:{
     title: "",
      
     done:{
       type: []
     }
   },
  data(){
    return {
      search: '',
      select:null,
      annee: 2018,
      items: [],
        headers: [
          {
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Codage OCID', value: 'record_ocid' },
          { text: 'Pays', value: 'country' },
          { text: 'Region', value: 'region' },
          { text: 'Secteur', value: 'sector' },
          { text: 'Titre', value: 'title' },
          { text: 'Montant', value: 'value' },
          { text: 'Dévise', value: 'currency' },
          { text: 'Etape', value: 'step' },
          { text: 'Dernière mise à jour', value: 'last_update' },
        ],
    }
  },
  mounted(){
    for(this.annee;this.annee<2032;this.annee++){
      this.items.push(this.annee)
    }
  },
  computed:{},
  methods:{
    onChange(value){
     if(value.length!=0){
       console.log(this.$store.state.idRegion)
      //  this.$store.dispatch('',this.$store.state.idRegion)
     }
    }
  }
}
</script>

