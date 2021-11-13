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
            <v-btn icon size="60"><v-icon size="60" color="white">mdi-menu-left</v-icon></v-btn>
            <span class="white--text font-weight-bold">2021</span>
            
            <v-btn icon size="60"><v-icon size="60" color="white">mdi-menu-right</v-icon></v-btn>
        </div>
       
       
     <v-btn-toggle
        mandatory
        color="primary"
        background-color="indigo"
        
    >   <v-hover >
            <v-btn height="100" width="200">
                $6,891.42M
                Budget
            </v-btn>
        
        </v-hover>  
       <v-hover>
            <v-btn height="100" width="200">
               $2,930.93M 
                Expense
            </v-btn>
        </v-hover><v-hover>
            <v-btn height="100" width="200">
                151
                Countries
            </v-btn>
        </v-hover><v-hover>
            <v-btn height="100" width="200">
                4,701
                Projects
            </v-btn>
        </v-hover><v-hover>
            <v-btn height="100" width="200">
               
                1,115
                Donors

            </v-btn>
        </v-hover>
    </v-btn-toggle>
</div>
</template>
