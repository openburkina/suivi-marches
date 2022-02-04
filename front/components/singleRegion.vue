<template>
  <v-card>
    <v-card-title>
      {{title}}
      <div width="100" class="ml-4">
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
        </div>
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
      items: [],
      annee:2018,
      select:null,

        headers: [
          {
            align: 'start',
            sortable: false,
            value: 'name',
          },
         
          { text: 'title', value: 'title' },
          { text: 'buyer_name', value: 'buyer_name' },
          { text: 'sector', value: 'sector' },
          { text: 'value', value: 'value' },
          { text: 'currency', value: 'currency' },
          { text: 'step', value: 'step' },
          { text: 'last_update', value: 'last_update' },
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

