<template>
    <div class="login">
        <h1 class="subheading grey--text">Login</h1>
         <v-container class="my-5">
             <v-layout row>
                <v-spacer></v-spacer>
                <v-flex xs-6> 
                    <v-card class="mb-3 px-3 py-3"> 
                        <v-form class="mb-3">
                            <v-text-field label="username" v-model="username"></v-text-field>
                            <v-text-field label="email" v-model="email"></v-text-field>
                            <v-text-field type="password" label="Password" v-model="password"></v-text-field>
                            <v-btn @click="login()" class="success ml-0" flat>Connection</v-btn>
                        </v-form>
                        <p>You don't have an account ? You can <router-link to="/signup">create one</router-link></p>
                    </v-card>
                </v-flex>
                <v-spacer></v-spacer>
             </v-layout>
         </v-container>
    </div>
</template>


<script>
import axios from 'axios'
export default {
    name: 'Login',
    data(){
        return{
            username: 'Benjamin',
            password: 'ps2Umj67)',
            email: 'rochez.benjamin@gmail.com'
        }
    },
    methods: {
        login(){
            const user = {
                username: this.username,
                password: this.password

            }

            axios.post('http://127.0.0.1:8000/api/rest-auth/login/', user)
            .then(res =>{
                console.log(res);
            })
            .catch(err =>{
                console.log(err)
            })
        }
    }
}
</script>


<style>

</style>