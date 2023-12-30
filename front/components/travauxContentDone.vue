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
      }"
       @click:row="createEditLink">
   
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
          { text: 'ID', value: 'record_ocid' },
          { text: 'Titre', value: 'title' },
          { text: 'Bailleur', value: 'buyer_name' },
          { text: 'Bénéficiaire', value: 'procuring_entity' },
          { text: 'Région', value: 'region' },
          { text: 'Secteur', value: 'sector' },
          { text: 'Statut', value: 'step' },
          { text: 'Entreprise exécutante', value: 'tenderers' },
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
    },
    createEditLink(project) {
      return this.$router.push({ path: '/travaux/' + project.id})
    },
  }
}
</script>

