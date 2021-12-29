<template>
  <v-carousel
    cycle
    height='570'
    hide-delimiter-background
    show-arrows-on-hover
  >
    <v-carousel-item
    >
      <v-sheet
        height="100%"
        width="100%"
      >
      <v-img
         :src="require('~/assets/img/image1.jpg')"
        ></v-img>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="text-h2">
          </div>
        </v-row>
      </v-sheet>
    </v-carousel-item>

    <v-carousel-item
    >
      <v-sheet
        height="100%"
        width="100%"
      >
      <v-img
         :src="require('~/assets/img/image2.jpg')"
        ></v-img>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="text-h2">
          </div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
    <v-carousel-item
    >
      <v-sheet
        height="100%"
        width="100%"
      >
      <v-img
         :src="require('~/assets/img/image3.jpg')"
        ></v-img>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="text-h2">
          </div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
    <v-carousel-item
    >
      <v-sheet
        height="100%"
        width="100%"
      >
      <v-img
         :src="require('~/assets/img/image4.jpg')"
        ></v-img>
        <v-row
          class="fill-height"
          align="center"
          justify="center"
        >
          <div class="text-h2">
          </div>
        </v-row>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>

<script>
  export default {
    data () {
      return {
        isXs: false,
        colors: [
          'indigo',
          'warning',
          'pink darken-2',
          'red lighten-1',
          'deep-purple accent-4',
        ],
        slides: [
          'First',
          'Second',
          'Third',
          'Fourth',
          'Fifth',
        ],
      }
    },
   mounted(){
       this.onResize();
        window.addEventListener("resize", this.onResize, { passive: true });
   },
    methods: {
        onResize() {
        this.isXs = window.innerWidth < 850;
        
        }
    }
  }
</script>