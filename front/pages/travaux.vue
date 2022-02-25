<template>
  <div>
    <Titre title="Travaux" />
    <v-card color="indigo lighten-5 elevation-4 mx-4 mt-4 mb-16">
      <v-card-title>
        Liste des Travaux
        
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Recherche"
          hide-details
          solo
          rounded
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="travaux"
        :search="search"
        :items-per-page=5
        :options=
        "{sortBy: []}"
        class="elevation-1"
        @click:row="createEditLink"
      >
        <template v-slot:[`item.statut`]="{ item }">
          <v-chip :color="getColor(item.statut)" dark>
            <v-icon size="24px">
              {{ getValue(item.statut) }}
            </v-icon>
          </v-chip>
        </template>
      </v-data-table>
    </v-card>
  </div>
</template>

<script>
export default {
  data(){
    return {
      search:'',
      headers: [
        {
            align: 'start',
            sortable: false,
         
          },
          
          { text: 'Ocid', value: 'record_ocid' },
          { text: 'Bailleur', value: 'buyer_name' },
          { text: 'Procuring', value: 'procuring_entity' },
          { text: 'Secteur', value: 'sector' },
          { text: 'Pays', value: 'country' },
          { text: 'Région', value: 'region' },
          { text: 'Montants', value: 'value' },
          { text: 'Etapes', value: 'step' },
          { text: 'Dernière Modification', value: 'last_update' },
        
      ],
    }
  },

  mounted(){
     this.$store.dispatch('AllTravaux')
  },
 
  computed:{
    travaux(){
      console.log(this.$store.state.listTravaux)
      return this.$store.state.listTravaux
    },
   
  },
  methods: {
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
    createEditLink(travaux) {
      this.$store.state.record_ocid = `Travaux : ${travaux.record_ocid}`
      return this.$router.push({ path: '/travaus/' + travaux.record_ocid})
    }
  }
}

</script>