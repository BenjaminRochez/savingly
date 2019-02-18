from rest_framework import routers
from recipes.viewsets import RecipeViewSet
from ingredients.viewsets import IngredientViewSet
from users.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'users', UserViewSet)
