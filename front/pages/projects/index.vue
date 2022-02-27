<template>
  <div>
   <Titre title="Travaux" />
    <v-card color="indigo lighten-5 elevation-4 mx-4 mt-4 mb-16">
      <v-card-title>
        Liste des travaux
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
        { text: 'ID', value: 'id' },
        { text: 'Titre', value: 'name' },
        { text: 'Bailleur', value: 'email' },
        { text: 'Bénéficiaire', value: 'country_name' },
        { text: 'Budget', value: 'region' },
        { text: 'Région', value: 'telephone' },
        { text: 'Secteur', value: 'contact_name' },
        { text: 'Statut', value: 'contact_name' },
       
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
    createEditLink(buyer) {
      this.$store.state.particularName = `Travaux de : ${buyer.name }`
      return this.$router.push({ path: '/projects/' + buyer.id})
    },
  },
}
</script>
