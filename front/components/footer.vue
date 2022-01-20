<template>
    <v-card
      flat
      tile
      fixed
      bottom
      class="indigo lighten-1 white--text text-center"
    >
      <v-card-text>
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4 white--text"
          icon
        >
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
        </v-btn>
      </v-card-text>
      <v-row
        justify="center"
        no-gutters
        >
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        to="/"
        >
       Home
      </v-btn>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        to="/projet"
        >
       Travaux
      </v-btn>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        to="/donors"
        >
       Bailleurs
      </v-btn>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        
        >
       Region
      </v-btn>
     
    </v-row>
      <v-card-text class="white--text pt-0">
        Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>Cafdo</strong>
      </v-card-text>
    </v-card>
</template>
<script>
  export default {
    data: () => ({
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  }
</script>
