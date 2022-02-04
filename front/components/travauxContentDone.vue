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
          { text: 'country', value: 'country' },
          { text: 'region', value: 'region' },
          { text: 'sector', value: 'sector' },
          { text: 'title', value: 'title' },
          { text: 'record_ocid', value: 'record_ocid' },
          { text: 'currency', value: 'currency' },
          { text: 'value', value: 'value' },
          { text: 'step', value: 'step' },
          { text: 'last_update', value: 'last_update' },
        ],
    }
  },
  methods:{
    clicked(row){
     
    }
  }
}
</script>

