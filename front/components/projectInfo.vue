<template>
  <v-card class="mx-auto" max-width="900">
    <Titre title="A propos du travail" />
    <v-list-item>
      <v-list-item-title>ID</v-list-item-title>
      <v-list-item-subtitle>{{ project.ocid }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Titre</v-list-item-title>
      <v-list-item-subtitle>{{ project.title }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>

    <v-list-item>
      <v-list-item-title>Bailleur</v-list-item-title>
      <v-list-item-subtitle>{{ project.buyer }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Bénéficiaire</v-list-item-title>
      <v-list-item-subtitle>{{ project.procuring_entity }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Budget</v-list-item-title>
      <v-list-item-subtitle>{{ project.budget }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Région</v-list-item-title>
      <v-list-item-subtitle>{{ project.region }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Secteur</v-list-item-title>
      <v-list-item-subtitle>{{ project.sector }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-list-item-title>Statut</v-list-item-title>
      <v-list-item-subtitle>{{ project.status }}</v-list-item-subtitle>
    </v-list-item>
    <v-divider></v-divider>
  </v-card>
</template>
<script>
import { mapState } from 'vuex'
export default {
//   computed: {
//     ...mapState('project', {
//       project: (state) => state.project,
//       errors: (state) => state.errors,
//     }),
//   },
    data() {
        return {
            project: {
                ocid: "OCDS_261-000",
                title: "Construction",
                buyer: "Entreprise X",
                procuring_entity: "Entreprise Y",
                budget: "215.000,00 MGA",
                region: "Analamanga, Madagascar",
                sector: "Santé",
                status: "Planification"
            }
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
  },
}
</script>