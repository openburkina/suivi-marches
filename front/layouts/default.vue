<template>
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      app
      temporary
    >
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title class="title">Calango</v-list-item-title>
            <v-list-item-subtitle>WEB</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider />

      <v-list dense>
        <v-list-item
          v-for="([icon, text, link], i) in items"
          :key="i"
          link
          @click="$vuetify.goTo(link)"
        >
          <v-list-item-icon class="justify-center">
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title class="subtitile-1 ml-2">{{
              text
            }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
     
      elevation="0"
      class="px-15 transparent"
     
    >
      <v-toolbar-title class="grey--text display-2">
      Cafdo
      </v-toolbar-title>
      <v-spacer />
      <v-app-bar-nav-icon
        v-if="isXs"
        class="ml-4"
        @click.stop="drawer = !drawer"
      />
      <div v-else>
        <v-btn text to="/inspire">
          <span class="mr-2">Home</span>
        </v-btn>
        <v-btn text to="/about">
          <span class="mr-2">Sobre</span>
        </v-btn>
        <v-btn text>
          <span class="mr-2">Download</span>
        </v-btn>
        <v-btn text>
          <span class="mr-2">Preços</span>
        </v-btn>
        <v-btn rounded outlined text>
          <span class="mr-2">Contatez-nous</span>
        </v-btn>
      </div>
    </v-app-bar>
    <v-main>
      <v-container>
        <Nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    isXs: false,
    items: [
      ["mdi-home-outline", "Home", "/inspire"],
      ["mdi-information-outline", "Sobre", "#features"],
      ["mdi-download-box-outline", "Download", "#download"],
      ["mdi-currency-usd", "Preços", "#pricing"],
      ["mdi-email-outline", "Contatos", "#contact"],
    ],
  }),
  watch: {
    isXs(value) {
      if (!value) {
        if (this.drawer) {
          this.drawer = false;
        }
      }
    },
  },
  
  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
  },
   methods: {
    onResize() {
      this.isXs = window.innerWidth < 850;
    },
  },

};
</script>
<style scoped>
.v-toolbar {
  transition: 0.6s;
}

.expand {
  height: 80px !important;
  padding-top: 10px;
}
</style>