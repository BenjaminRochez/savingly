import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/recipes',
      name: 'recipes',
      component: () => import(/* webpackChunkName: "recipes" */ './views/Recipes.vue')
    },
    {
      path: '/recipe/:recipe_id',
      name: 'ViewRecipe',
      component: () => import(/* webpackChunkName: "recipes" */ './views/ViewRecipe.vue')
    }
  ]
})
