<template>
  <div>
    <p class="display-2 text-center font-weight-bold mb-10 mt-16">Liste de Bailleurs  <span id="explore"></span></p>
    <Title value="Liste des projets"></Title>
    <v-card color="indigo lighten-5 elevation-4 mx-4 mt-4 mb-16">
      <v-card-title>
        Bailleurs
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Recherche"
          single-line
          hide-details
          solo
          rounded
        ></v-text-field>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="buyers"
        :search="search"
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
        { text: 'name', value: 'name' },
        { text: 'email', value: 'email' },
        { text: 'country_name', value: 'country_name' },
        { text: 'locality', value: 'locality' },
        { text: 'telephone', value: 'telephone' },
        { text: 'latitude', value: 'latitude' },
        { text: 'longitude', value: 'longitude' },
        { text: 'contact_name', value: 'contact_name' },
        { text: 'region', value: 'region' },
        { text: 'url', value: 'url' },
        { text: 'uri', value: 'uri' },
        { text: 'fax_number', value: 'fax_number' },
        { text: 'scheme', value: 'scheme' },
        { text: 'legal_name', value: 'legal_name' },
        { text: 'postal', value: 'postal' },

       
      ],
    }
  },

  mounted(){
     this.$store.dispatch('fetchBuyers')
  },
 
  computed:{
    buyers(){
      return this.$store.state.list
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
      return this.$router.push({ path: '/works/' + buyers.id })
    },
  },
}
</script>
<style lang="scss" scoped>

#explore{
    background-color: #5C6BC0;
    width: 80px;
    height: 8px;
    margin: 0 auto;
    display: block;
    margin-top: 10px;
}
</style>
