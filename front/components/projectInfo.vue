<template>
<div>
    <Titre title="A propos du travail" />
  <v-card class="mx-auto" max-width="900">
    <v-list-item>
      <v-list-item-title>ID</v-list-item-title>
      <v-list-item-subtitle>{{ info.ocid }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Titre</v-list-item-title>
      <v-list-item-subtitle>{{ info.title }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>

    <v-list-item>
      <v-list-item-title>Bailleur</v-list-item-title>
      <v-list-item-subtitle>{{ info.buyer }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Bénéficiaire</v-list-item-title>
      <v-list-item-subtitle>{{ info.procuring_entity }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Budget</v-list-item-title>
      <v-list-item-subtitle>{{ info.budget }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Région</v-list-item-title>
      <v-list-item-subtitle>{{ info.region }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Secteur</v-list-item-title>
      <v-list-item-subtitle>{{ info.sector }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Statut</v-list-item-title>
      <v-list-item-subtitle>{{ info.status }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
  </v-card>
</div>

</template>
<script>
export default {
  props: ['info'],
  methods: {
    getColor(statut) {
      if (statut < 1) return '#00E396'
      else return '#008FFB'
    },
    getValue(statut) {
      if (statut < 1) return 'mdi-close'
      else return 'mdi-check'
    },
  },
}
</script>