<template>
    <nav>
        <v-toolbar app>
            <v-toolbar-title class="headline text-uppercase">
                <span>Saving</span>
                <span class="font-weight-light">ly</span>
            </v-toolbar-title>
      
        </v-toolbar>

        <v-navigation-drawer v-model="drawer" app  class="primary"> 
            <v-layout column align-center>
                <v-flex class="mt-5 text-xs-center">
                    <v-avatar size='100'>
                        <img src="https://dummyimage.com/100x100/000/fff" alt="">
                    </v-avatar>

                </v-flex>
            
            </v-layout>
            <v-list>
                <v-list-tile v-for="link in links" :key="link.text" router :to="link.route">
                    <v-list-tile-action>
                        <v-icon class="white--text">{{ link.icon }}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-content>
                        <v-list-tile-title class="white--text">{{ link.text }}</v-list-tile-title>
                    </v-list-tile-content>
                </v-list-tile>
            </v-list>
        </v-navigation-drawer>
    </nav>
</template>

<script>

export default {
    name: 'Navbar',
    data(){
        return{
            drawer: true,
            links: [
                {icon: 'dashboard', text: 'Dashboard', route: '/dashboard'},
                {icon: 'folder', text: 'Recipes', route: '/recipes'},
                {icon: 'person', text: 'Ingredients', route: '/ingredients'},
                
            ],
            
        }
    },
    methods: {
       
    },
    
    watch:{
        
    
    } 
}
</script>

<style>
.v-list__tile--active {
    border-left: 4px solid #3cd1c2;
}
</style>
