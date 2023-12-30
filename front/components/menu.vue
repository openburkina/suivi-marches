<template>
  <v-menu
        bottom
        origin="center center"
        transition="fab-transition"
        nudge-bottom="30"
        open-on-hover :close-on-content-click="false"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
          text
          class="white--text"
            v-bind="attrs"
            v-on="on"
          >
          Region
          <v-icon class="ml-4"> mdi-chevron-down</v-icon>
          </v-btn>
        </template>
        <v-card>
          <v-list-item-content class="justify-center">
            <div class="mx-auto text-center">
             
              <v-btn
                depressed
                text
                to="/about"
              >
                <v-icon class="mx-3">
                  mdi-information-variant
                </v-icon>
                <span class="mx-2">
                  About us
                </span>
              </v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn
                depressed
                text
                to="/download"
              >
              <v-icon class="mx-3">
                mdi-tray-arrow-down
              </v-icon>
              <span class="mx-2"> Download </span>
              </v-btn>
            </div>
          </v-list-item-content>
        </v-card>
      </v-menu>
</template>

<script>
export default {

}
</script>
