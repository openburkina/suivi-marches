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
            <v-list-item-title class="title">Cafdo</v-list-item-title>
            <v-list-item-subtitle>WEB</v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider />

      <v-list
        nav
        dense
      >
        <v-list-item-group
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item to="/">
            <v-list-item-icon>
              <v-icon>mdi-home</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item>

          <v-list-item to="projet">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Projects</v-list-item-title>
          </v-list-item>
          
          <v-list-item to="/donors">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>Donors</v-list-item-title>
          </v-list-item>
          
          <v-list-item to="/sustainable">
            <v-list-item-icon>
              <v-icon>mdi-account</v-icon>
            </v-list-item-icon>
            <v-list-item-title>SUSTAINABLE DEVELOPMENT GOALS</v-list-item-title>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-parallax
      height="750"
      :src="require('~/assets/img/bgHero.jpg')"
    >
    <v-app-bar
      height="90"
      elevation="0"
      fixed
      v-bind:color="scrollPosition>28?'light-blue darken-4':'transparent'"
    >
    <v-avatar
      size="90"
      >
    <img
       :src="require('~/assets/img/icon3.png')" height="40" width="40"
      >
    </v-avatar>
      <v-spacer />
      <v-app-bar-nav-icon
        v-if="isXs"
        class="ml-2"
        color="white"
        @click.stop="drawer = !drawer"
      />
      <div v-else>
        <v-btn to="/" text>
          <span class="mr-2 white--text">Home</span>
        </v-btn>
        <v-btn to="/projet" text>
          <span class="mr-2  white--text">Projects</span>
        </v-btn>
        <v-btn text to="/donors">
          <span class="mr-2  white--text">Donors</span>
        </v-btn>
        <v-btn text to="/sustainable">
          <span class="mr-2  white--text">SUSTAINABLE DEVELOPMENT GOALS</span>
        </v-btn>
        <v-btn text to="/approche">
          <span class="mr-2  white--text">OUR APPROACHES</span>
        
        </v-btn>
            <v-menu
        bottom
        origin="center center"
        transition="fab-transition"
        
        nudge-bottom="40"
        open-on-hover :close-on-content-click="false"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
          text
          class="white--text"
            v-bind="attrs"
            v-on="on"
          >
           More
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
               About us
              </v-btn>
              <v-divider class="my-3"></v-divider>
              <v-btn
                depressed
                text
                to="/download"
              >
                Download
              </v-btn>
              
            </div>
          </v-list-item-content>
        </v-card>
          
      </v-menu>
      </div>
    </v-app-bar>
    <Parallax />
    </v-parallax>
    <v-main>
      <v-container fluid>
       <Nuxt />
     
      </v-container>
    </v-main>
    <v-scale-transition>
      <v-btn
        fab
        dark
        fixed
        bottom
        right
        color="secondary"
      
      >
        <v-icon>mdi-arrow-up</v-icon>
      </v-btn>
    </v-scale-transition>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    isXs: false,
    scrollPosition: null,

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
    window.addEventListener('scroll', this.updateScroll);

  },
   methods: {
    onResize() {
      this.isXs = window.innerWidth < 850;
    },
    updateScroll() {
       this.scrollPosition = window.scrollY
    }
    
  },
  

};
</script>
<style scoped>
.v-toolbar {
  transition: 0.6s;
}

</style>

