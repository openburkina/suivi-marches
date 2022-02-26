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
        { text: 'Date', value: 'dec_date' },
        { text: 'Montant', value: 'amount_dec' },
        { text: 'Livrable', value: 'deliverable' },
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