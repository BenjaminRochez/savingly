<template>
    <div>
        <h1 class="subheading grey--text">Recipes</h1>
        <v-container class="my-5">
            <v-expansion-panel flat>
                <v-expansion-panel-content v-for="recipe in recipes" :key='recipe.id'>
                    <div slot="header">{{recipe.name}}</div>
                    <v-card>
                        <v-card-text class="px-4 grey--text">
                            <div class="font-weight-bold">{{recipe.name}}</div>
                            <div>{{recipe.body}}</div>
                            <router-link tag="li" :to="{name:'ViewRecipe', params: {recipe_id: recipe.id}}"> <v-btn class="warning">See the recipe</v-btn></router-link>
                             <v-btn class="warning" @click="deleteRecipe(recipe.id)">Delete</v-btn>
                        </v-card-text>
                    </v-card>
                </v-expansion-panel-content>
            </v-expansion-panel>
        </v-container>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'Recipes',

    data(){
        return{
            recipes: [],
            ingredients: [],
            loading: false
        }
    },
    methods: {
        getRecipes(){
            this.loading = true;
            axios.get('http://127.0.0.1:8000/api/recipes/')
            .then(res =>{     
                this.recipes = res.data;
            })
            .catch(err => {
                // eslint-disable-next-line
                console.log('Error: ' + err)
            })
        },
        deleteRecipe(id){
            this.loading = true;
            axios.delete(`http://127.0.0.1:8000/api/recipes/${id}/`).then(() =>{
                this.loading = false;
                this.getRecipes();
            }).catch(err =>{
            this.loading = false;
            // eslint-disable-next-line
            console.log(err)
            })
        }
    },
    created(){
      this.getRecipes();  
    },
    computed: {
        
    }
}
</script>

