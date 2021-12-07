<template>
  <v-simple-table height="300px">
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            Name
          </th>
          <th class="text-left">
            Scheme
          </th>
          <th class="text-left">
            Action
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="buyer in buyers"
          :key="buyer.id"
        >
          <td>{{ buyer.name }}</td>
          <td>{{ buyer.identifier.scheme}}</td>
          <td>
            <nuxt-link
            :to="`/works/${buyer.id}`"
            >
              Ses Travaux
            </nuxt-link>
          </td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
</template>

<script>
export default {

  mounted(){
     this.$store.dispatch('fetchBuyers')
  },
 
  computed:{
    buyers(){
      return this.$store.state.list
    }
  },
  methods:{
  
  }
}
</script>

