<template>
    <div v-if="$vuetify.breakpoint.xs ||$vuetify.breakpoint.sm">
        <v-btn-toggle
        borderless
        background-color="white"
            
        >   
        <v-btn height="100" width="190" id="id" color="primary">
            $6,891.42M
            Budget
        </v-btn>
        <v-btn height="100" width="190" id="id" color="primary">
            $2,930.93M 
            Expense
        </v-btn>
        </v-btn-toggle>
        <v-btn-toggle
        borderless
        background-color="white"
        >
            <v-btn height="100" width="150" id="id" color="primary">
            151
            Countries
            </v-btn>
            <v-btn height="100" width="150" id="id" color="primary">
                4,701
                Projects
            </v-btn>
            <v-btn height="100" width="150" id="id" color="primary">
                1,115
                Donors
            </v-btn>
        </v-btn-toggle>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoop lang="scss">
#id:hover{
  transform: scale(1.15);
  border-radius: 10px 10px 10px 10px;
  opacity: 100%;
  z-index:10;
  transition: width 1s, height 1s, transform 1s;
  
}

</style>