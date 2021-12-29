<template>
<div>
        <p class="white--text font-weight-bold mx-auto display-1">
        UNDP Transparency Portal
        </p>
        <p class="white--text mx-auto">
            In UNDP, we are committed to eradicating poverty, fighting climate change and reducing
        </p>
        <p class="white--text mx-auto">
            inequalities and exclusion around the world. Discover how, with the help of our partners, we work 
            day to day to make this a reality.
        </p>
    <v-text-field
        placeholder="Search using Project,Donors, Recipients or Keyword"
        solo
        clearable
        append-icon="mdi-magnify"
        style="width: 500px;"
        class="mx-auto mt-5"
        
    > 
    </v-text-field>
     <div class="mx-auto py-5 mb-5">
        <v-btn icon size="60"><v-icon size="60" color="`disable=='disabled'?transparent:white`" disable @click="decrease">mdi-menu-left</v-icon></v-btn>
        <span class="white--text font-weight-bold">{{ date }}</span>
        
        <v-btn icon size="60"><v-icon size="60" color="white" @click="increment">mdi-menu-right</v-icon></v-btn>
    </div>
       
    <ButtonGroup />
    <ResponsiveButtonGroup />
    
</div>
</template>
<script>

export default {
    data(){
        return {
            date:2021,
            disable:null,
            color:null
        }
    },
    methods:{
        increment(){
            return this.date++
        },
        decrease(){
            if(this.date<=2018) return this.disabled = "disabled" & this.color=="transparent"
            return this.date--

        }
    }
}
</script>

<style scoped>
.v-btn i:hover{
  transform: scale(2.15);
  transition: width 1s, height 1s, transform 1s;

}
</style>