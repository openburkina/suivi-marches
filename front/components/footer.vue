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
       A propos
      </v-btn>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        to="/projet"
        >
       Partenaires
      </v-btn>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        to="/donors"
        >
        Termes d’utilisation
      </v-btn>
      <v-btn
        color="white"
        text
        rounded
        class="my-2"
        
        >
       Telecharger
      </v-btn>
     
    </v-row>

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
