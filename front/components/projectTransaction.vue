<template>
  <div>
    <Titre title="Transactions liées au travail" />
    <v-card class="mx-auto px-3">
      <v-data-table
        :headers="headersDecaissements"
        :items="amounts"
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
      
      headersDecaissements: [
        { text: 'Date', value: 'date' },
        { text: 'Montant', value: 'amount' },
        { text: 'Livrable', value: 'item' },
      ],
    }
  },
//   computed:{
//       ...mapState('project', {
//         amounts: state=> state.amounts,
//         errors: state=> state.errors
//       })
//     },
}
</script>