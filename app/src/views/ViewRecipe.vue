<template>
    <div>
         <h1 class="subheading grey--text">View Recipe</h1>
            <p>Name: {{recipe.name}}</p>
            <div class="summary">
                <ul>
                    <li>{{recipe.quantity}} Pers.</li>
                    <li>{{recipe.preparation_time}} Min</li>
                    <li>{{recipe.cooking_time}} Min</li>
                    <li>{{recipe.difficulty}}</li>
                </ul>
            </div>
            <p v-html="recipe.body"></p>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'ViewRecipe',
    data(){
        return{
            recipe:  [],
            recipeId: this.$route.params.recipe_id
        }
    },
    methods: {
        updateId(){
            this.recipeId = this.$route.params.recipe_id;    
        },
        getRecipes(){
            this.loading = true;
            axios.get(`http://127.0.0.1:8000/api/recipes/${this.recipeId}/`)
            .then(res =>{     
                this.recipe = res.data;
                console.log(this.recipe.body)
            })
            .catch(err => {
                // eslint-disable-next-line
                console.log('Error: ' + err)
            })
        }
    },
    watch: {
        $route: 'updateId',
    },
    created(){
        this.getRecipes(this.recipeId)
    }
}
</script>

