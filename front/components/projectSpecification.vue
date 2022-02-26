<template>
  <v-card class="mx-auto px-3">
    <Titre title="Etapes du travail" />
    <v-data-table
      :headers="headers"
      :items="activities"
      :search="search"
      class="elevation-0"
    >
    </v-data-table>
  </v-card>
</template>
<script>

import {  mapState } from 'vuex'

export default {
  props: ['search'],
  data() {
    return {
      headers: [
        { text: 'Date début', value: 'start_date' },
        { text: 'Date fin', value: 'finish_date' },
        { text: 'Montant', value: 'amount_act' },
        { text: "Acteurs d'éxecutions", value: 'Actors_execution' },
        { text: 'Acteurs partenaires', value: 'Actors_partner' },
        { text: 'Année de planifications', value: 'year_plan' },
      ],
    }
  },
//   computed:{
//       ...mapState('project', {
//         activities: state=> state.activities,
//         errors: state=> state.errors
//       })
//     },
}
</script>