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


            <ul>
                <li v-for="ingredient in ingredients" :key="ingredient.id">{{ingredient.name}}</li>
            </ul>
            {{ingredients}}
            <h3>Price</h3>
            <p>{{price}}</p>
            

    </div>
</template>

<script>
import axios from 'axios'
export default {
    name:'ViewRecipe',
    data(){
        return{
            recipe:  [],
            ingredientsList: [],
            ingredients: [],
            price: 0,
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
                this.ingredientsList = res.data.ingredients;
                this.getIngredients();
            })
            .catch(err => {
                // eslint-disable-next-line
                console.log('Error: ' + err)
            })
        },
        getIngredients(){
            this.ingredientsList.forEach((el) =>{
                
                axios.get(`http://127.0.0.1:8000/api/ingredients/${el}/`)
                .then(res =>{
                    this.ingredients.push(res.data);   
                    this.price += res.data.price;
                })            
            })
        },
    },
    watch: {
        $route: 'updateId',
    },
    created(){
        this.getRecipes(this.recipeId);
    },
}
</script>

