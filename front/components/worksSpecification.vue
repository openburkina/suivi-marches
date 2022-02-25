<template>
  <v-card>
    <v-card-title>
      {{title}}
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
     title:"",
     done:{
       type: []
     }
   },
  data(){
    return {
      search: '',
        headers: [
          {
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Item', value: 'record_ocid' },
          { text: 'Value', value: 'country' },
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
  methods:{
    clicked(row){
     
    }
  }
}
</script>

