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
      :items=inprogress
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
     inprogress:{
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
          { text: 'url', value: 'url' },
          { text: 'compiled_release', value: 'compiled_release' },
        ],
    }
  },
  methods:{
    clicked(row){
     
    }
  }
}
</script>

