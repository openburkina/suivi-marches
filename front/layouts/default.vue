<template>
  <v-app>
      <v-parallax
        height="700"
        :src="require('~/assets/img/bgHero.jpg')"
      >
      <Parallax />
    </v-parallax>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      app
      fixed
      temporary
    >
      <v-list>
        <v-list-item>
          <v-list-item-content>
              <img
                :src="require('~/assets/img/pnud.png')" height="100"
              >
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
    <v-app-bar
      app
      fixed
      height="90"
      v-bind:elevation="scrollPosition>28?4:0"
      v-bind:color="scrollPosition<28?'transparent':'indigo lighten-1'"
    >
        <img
          :src="require('~/assets/img/logo.png')" height="60" width="50"
        >
  
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
      </div>
    </v-app-bar>
    <v-main>
      <v-container>
       <Nuxt />
      </v-container>
        <Footer />
    
    </v-main>
    <v-scale-transition>
      <v-btn
        v-scroll="onScroll"
        v-show="fab"
        fab
        dark
        fixed
        bottom
        right
        color="indigo lighten-1"
        @click="toTop"
        elevation="10"
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
    miniVariant:false,
    fab: false,
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
    },
    onScroll (e) {
      if (typeof window === 'undefined') return
      const top = window.pageYOffset ||   e.target.scrollTop || 0
      this.fab = top > 20
    },
    toTop () {
      this.$vuetify.goTo(0)
    }
  },
  
};
</script>
<style scoped>
.v-toolbar {
  transition: 0.6s;
}
active-class{
  color:red;
}

.v-btn{
  z-index:999;
}

</style>

