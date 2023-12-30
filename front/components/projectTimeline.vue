<template>
  <div class="container">
    <Titre title="Phases du travail" />
    <v-card v-if="dates.id" class="mx-auto px-3 elevation-0">
      <v-timeline>
        <v-timeline-item right :color="colorClass.stage" icon="mdi-calendar-check" fill-dot>
          <v-card>
            <v-card-title :class="colorClass.stage" class="white--text">
              {{ dates.award_period.end_date }}
            </v-card-title>
            <v-card-text class="white pt-2">
              Fin de la phase d'attribution
            </v-card-text>
          </v-card>
        </v-timeline-item>
        
        <v-timeline-item left :color="colorClass.event" v-for="award of dates.awards" :key="award.id" icon="mdi-file-sign" fill-dot>
          <v-card>
            <v-card-title :class="colorClass.event" class="white--text">
              {{ award.date }}
            </v-card-title>
            <v-card-text class="white pt-2">
              Attribution 
              <p>
                Période contractuelle : Du {{ award.contract_period.start_date }} au {{ award.contract_period.end_date }}
              </p> 
            </v-card-text>
          </v-card>
        </v-timeline-item>

        <v-timeline-item right :color="colorClass.stage" icon="mdi-calendar-clock" fill-dot>
          <v-card>
            <v-card-title :class="colorClass.stage" class="white--text">
              {{ dates.award_period.start_date }}
            </v-card-title>
            <v-card-text class="white pt-2">
              Début de la phase d'attribution
            </v-card-text>
          </v-card>
        </v-timeline-item>
        <v-timeline-item right :color="colorClass.stage" icon="mdi-calendar-check" fill-dot>
          <v-card>
            <v-card-title :class="colorClass.stage" class="white--text">
              {{ dates.tender_period.end_date }}
            </v-card-title>
            <v-card-text class="white pt-2">
              Fin de l'appel d'offre
            </v-card-text>
          </v-card>
        </v-timeline-item>
        <v-timeline-item right :color="colorClass.stage" icon="mdi-calendar-clock" fill-dot>
          <v-card>
            <v-card-title :class="colorClass.stage" class="white--text">
              {{ dates.tender_period.start_date }}
            </v-card-title>
            <v-card-text class="white pt-2">
              Début de l'appel d'offre
            </v-card-text>
          </v-card>
        </v-timeline-item>
      </v-timeline>
    </v-card>
  </div>
</template>
<script>
export default {
  props: ['search', 'dates'],
  data() {
    return {
      colorClass: {
        stage: "red lighten-2",
        event: "indigo lighten-1"
      },
      // dates: {
      //   tender_period: {
      //     start: "22 Novembre 2021",
      //     end: "22 Novembre 2021"
      //   },
      //   award_period: {
      //     start: "23 Novembre 2021",
      //     end: "22 Novembre 2022"
      //   },
      //   awards: [
      //     {
      //       date: "25 Novembre 2021",
      //       contract_period: {
      //         start: "01 Janvier 2022",
      //         end: "31 Janvier 2022"
      //       }
      //     },
      //     {
      //       date: "01 Decembre 2021",
      //       contract_period: {
      //         start: "01 Janvier 2022",
      //         end: "31 Janvier 2022"
      //       }
      //     },
      //     {
      //       date: "29 Decembre 2021",
      //       contract_period: {
      //         start: "01 Janvier 2022",
      //         end: "31 Janvier 2022"
      //       }
      //     },
      //   ]
      // }
    }
  },
}
</script>