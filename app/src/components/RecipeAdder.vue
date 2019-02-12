<template>
    <v-dialog max-width="600px" v-model="dialog">
        <v-btn flat slot="activator" class="success">Add new recipe</v-btn>
        <v-card>
            <v-card-title>Add a new recipe</v-card-title>
            <v-card-text>
                <v-form class='px-3' ref="form">
                    <v-text-field label="Nom de la recette" prepend-icon="receipt" v-model="name"></v-text-field>
                    <v-textarea label="Etapes de la recette" v-model="body" prepend-icon='edit'></v-textarea>
                    <v-text-field label="Quantité (Pers.)" prepend-icon="person" v-model="quantity"></v-text-field>
                    <v-text-field label="Preparation Time" prepend-icon="person" v-model="preparation_time"></v-text-field>
                    <v-text-field label="Cooking Time" prepend-icon="person" v-model="cooking_time"></v-text-field>
                    <v-select :items="items" v-model="difficulty" label="difficulty"></v-select>
                    
                    <v-textarea label="Astuces" v-model="hint" prepend-icon='edit'></v-textarea>

                    <v-spacer></v-spacer>

                    <v-btn flat class="success mx-0 mt-3" @click='submit()' :loading='loading'>Add a recipe</v-btn>
                </v-form>
            </v-card-text>
        </v-card>
    </v-dialog>
</template>


<script>
import axios from 'axios'
export default {
    name: 'RecipeAdder',
    data(){
        return{
            name: '',
            items: ['Easy', 'Medium', 'Advanced'],
            body: '',
            quantity: '',
            preparation_time: '',
            cooking_time: '',
            difficulty: 'Easy',
            hint: '',
            author: 1,
            loading: false,
            dialog: false
        }
    },
    methods: {
        submit(){
            const recipe = {
                name: this.name,
                body: this.body,
                quantity: this.quantity,
                preparation_time: this.preparation_time,
                cooking_time: this.cooking_time,
                //difficulty: this.difficulty,
                hint: this.hint,
                author: this.author
            }
            this.loading = true;

            axios.post('http://127.0.0.1:8000/api/recipes/', recipe)
            .then(res =>{
                this.loading = false;
                this.dialog = false;

            })
            .catch(err =>{
                // eslint-disable-next-line
                console.log(err)
            })
        },

    }
}
</script>
