<template>
    <v-sheet>
        <Tabs />
        <div class="grey--text font-weight-bold display-4">
           
        </div>
    </v-sheet>
</template>
<script>
export default {
    mounted(){
        this.$store.dispatch('myActions')
    },
   computed:{
       data(){
           return this.$store.state.data
       }
   }
}
</script>