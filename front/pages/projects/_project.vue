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
          Infos
          <v-icon>mdi-axis-arrow-info</v-icon>
        </v-tab>

        <v-tab href="#tab-2">
          Spécifications
          <v-icon>mdi-format-list-text</v-icon>
        </v-tab>

        <v-tab href="#tab-3">
          Décaissements
          <v-icon>mdi-cash</v-icon>
        </v-tab>

        <v-tab href="#tab-4">
          Chronologie
          <v-icon>mdi-chart-timeline</v-icon>
        </v-tab>
      </v-tabs>

      <v-tabs-items v-model="tab" class="mb-9">
        <v-tab-item value="tab-1" class="mb-9">
          <ProjectInfo :project="getProjet()" />
        </v-tab-item>
        <v-tab-item value="tab-2">
          <ProjectSpecification  :search="search" />
        </v-tab-item>
        <v-tab-item value="tab-3">
          <ProjectTransaction :search="search"/>
        </v-tab-item>
        <v-tab-item value="tab-4">
          <ProjectTimeline :search="search"/>
        </v-tab-item>
      </v-tabs-items>
    </v-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      search: '',
      id: this.$route.params.project,
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
      return `${message} sur le projet : ${this.id}`
    },
    getProjet() {
        console.log(this.id)
      return this.projets.find((p) => p.id == this.id)
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