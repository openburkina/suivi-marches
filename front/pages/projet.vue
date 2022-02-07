<template>
  <div>
   <Titre title="Liste de Bailleurs" />
    <Title value="Liste des projets"></Title>
    <v-card color="indigo lighten-5 elevation-4 mx-4 mt-4 mb-16">
      <v-card-title>
        Bailleurs
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
        :items="buyers"
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
        { text: 'id', value: 'id' },
        { text: 'Nom', value: 'name' },
        { text: 'Email', value: 'email' },
        { text: 'Pays', value: 'country_name' },
       // { text: 'Localité', value: 'locality' },
        { text: 'Région', value: 'region' },
        { text: 'telephone', value: 'telephone' },
       // { text: 'latitude', value: 'latitude' },
       // { text: 'longitude', value: 'longitude' },
        { text: 'Nom du Contact', value: 'contact_name' },
        // { text: 'legal_name', value: 'legal_name' },
        // { text: 'postal', value: 'postal' },
        // { text: 'url', value: 'url' },
        // { text: 'uri', value: 'uri' },
        // { text: 'fax_number', value: 'fax_number' },
        // { text: 'scheme', value: 'scheme' },
       
      ],
    }
  },

  mounted(){
     this.$store.dispatch('fetchBuyers')
  },
 
  computed:{
    buyers(){
      return this.$store.state.list
    },
    done(){
      return this.$store.state.recordsDone.length
    },
    pregress(){
      return this.$store.state.recordsInprogress.length
    }
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
    createEditLink(buyers) {
      this.$store.state.particularName = `Travaux de : ${buyers.name }`
      return this.$router.push({ path: '/projets/' + buyers.id})
    },
  },
}
</script>
