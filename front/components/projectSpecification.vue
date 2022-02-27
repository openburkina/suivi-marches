<template>
<div>
  <Titre title="Etapes du travail" />
  <v-card class="mx-auto px-3">
    <v-data-table
      :headers="headers"
      :items="activities"
      :search="search"
      class="elevation-0"
    >
    </v-data-table>
  </v-card>
</div>
</template>
<script>

import {  mapState } from 'vuex'

export default {
  props: ['search'],
  data() {
    return {
      headers: [
        { text: 'Description', value: 'description' },
        { text: 'Quantité', value: 'quantity' },
        { text: 'Valeur unitaire', value: 'unitValue' }
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