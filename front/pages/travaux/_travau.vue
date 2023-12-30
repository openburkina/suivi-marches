<template>
  <div>
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
          <ProjectInfo :info="info" />
        </v-tab-item>
        <v-tab-item value="tab-2">
          <ProjectSpecification  :search="search"  :items="items"/>
        </v-tab-item>
        <v-tab-item value="tab-3">
          <ProjectTransaction :search="search" :transactions="transactions"/>
        </v-tab-item>
        <v-tab-item value="tab-4">
          <ProjectTimeline :search="search" :dates="dates"/>
        </v-tab-item>
      </v-tabs-items>
  </div>
</template>
<script>
  import { mapState, mapActions } from 'vuex';

  export default {
    computed: {
      ...mapState({
        info: 'projectInfo',
        items: 'projectItems',
        dates: 'projectStages',
        transactions: 'projectTransactions'
      })
    },

    mounted() {
      console.log(this.id)
      this.fetchProjectInfo(this.id);
      this.fetchProjectItems(this.id);
      this.fetchProjectStages(this.id);
      this.fetchProjectTransactions(this.id);
    },

    data() {
      return {
        search: '',
        id: this.$route.params.travau,
        tab: null,
      }
    },

    methods: {
      ...mapActions([
        'fetchProjectInfo',
        'fetchProjectItems',
        'fetchProjectStages',
        'fetchProjectTransactions'
      ]),
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