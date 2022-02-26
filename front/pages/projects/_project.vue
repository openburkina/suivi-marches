<template>
  <div>
    <v-card>
      <v-tabs
        v-model="tab"
        background-color="indigo lighten-5"
        centered
        icons-and-text
      >
        <v-tabs-slider></v-tabs-slider>

        <v-tab href="#tab-1">
          Info
          <v-icon>mdi-axis-arrow-info</v-icon>
        </v-tab>

        <v-tab href="#tab-2">
          Activités
          <v-icon>mdi-archive</v-icon>
        </v-tab>

        <v-tab href="#tab-3">
          Décaissements
          <v-icon>mdi-bank</v-icon>
        </v-tab>

        <v-tab href="#tab-4">
          Indicateurs
          <v-icon>mdi-arrow-projectile</v-icon>
        </v-tab>
      </v-tabs>

      <!-- <v-tabs-items v-model="tab" class="mb-9">
        <v-tab-item value="tab-1" class="mb-9">
          <TabInfoProjet :projet="getProjet()" />
        </v-tab-item>
        <v-tab-item value="tab-2">
          <TabActiviteProjet  :search="search" />
        </v-tab-item>
        <v-tab-item value="tab-3">
          <TabDecaissementProjet :search="search"/>
        </v-tab-item>
        <v-tab-item value="tab-4">
          <TabIndicateurProjet :search="search"/>
        </v-tab-item>
      </v-tabs-items> -->
    </v-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      search: '',
      idProjet: this.$route.params.id,
      tab: null,
      projets: [
        {
          id: 78366,
          bailleur: 'UNSFC',
          executant: 'EXC 780',
          secteur: 'Santé',
          région: 'Iraq',
          statut: 1,
          budget: 12849585.94,
          dateDerniereMAJ: '2021-12-12',
        },
        {
          id: 88466,
          bailleur: 'JIJN',
          executant: 'LONM 754',
          secteur: 'Agricutlure',
          région: 'Afghanistan',
          statut: -1,
          budget: 8779344.94,
          dateDerniereMAJ: '2021-11-23',
        },
        {
          id: 90475,
          bailleur: 'NJDD',
          executant: 'OLNM 098',
          secteur: 'Sécurité',
          région: 'Iraq',
          statut: -1,
          budget: 78578.94,
          dateDerniereMAJ: '2021-09-12',
        },
      ],
    }
  },
  methods: {
    getTitle(message) {
      return `${message} sur le projet : ${this.idProjet}`
    },
    getProjet() {
      return this.projets.find((p) => p.id == this.idProjet)
    },
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