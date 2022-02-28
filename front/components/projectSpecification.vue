<template>
<div>
  <Titre title="Etapes du travail" />
  <v-card class="container mx-auto px-3">
    <v-data-table
      :headers="headers"
      :items="items"
      :search="search"
      class="elevation-0"
    >
    </v-data-table>
  </v-card>
</div>
</template>
<script>
export default {
  props: ['search', 'items'],
  data() {
    return {
      headers: [
        { text: 'Description', value: 'description' },
        { text: 'Quantité', value: 'quantity' },
        { text: 'Valeur unitaire', value: 'unit_value' }
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