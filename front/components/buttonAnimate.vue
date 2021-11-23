<template>
    <v-btn-toggle
        borderless
        rounded
        background-color="white"
    >   
    <v-btn height="130" width="200" id="id">
        $6,891.42M
        Budget
    </v-btn>
    <v-btn height="130" width="200" id="id">
        $2,930.93M 
        Expense
    </v-btn>
    <v-btn height="130" width="200" id="id">
        151
        Countries
    </v-btn>
    <v-btn height="130" width="200" id="id">
        4,701
        Projects
    </v-btn>
    <v-btn height="130" width="200" id="id">
        1,115
        Donors
    </v-btn>
    </v-btn-toggle>
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
  background-color: #5C6BC0;
  color: white;
  z-index:10;
  
}
.v-btn-toggle{
    background-color: red;
}

</style>