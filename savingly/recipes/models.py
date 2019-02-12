from django.db import models
from ingredients.models import Ingredient
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    EASY = 'Easy'
    MEDIUM = 'Medium'
    ADVANCED = 'Advanced'


    DIFFICULTY_CHOICES = (
        (EASY, "Easy"),
        (MEDIUM, "Medium"),
        (ADVANCED, "Advanced")
    )


    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=True)
    recipe_summary = models.TextField(blank=True) 
    ingredients = models.ManyToManyField(Ingredient, blank=True)

    quantity = models.IntegerField(default=0, blank=True)

    preparation_time = models.IntegerField(default=0, blank=True)
    cooking_time = models.IntegerField(default=0, blank=True)

    difficulty = models.CharField(max_length=10,
                                choices=DIFFICULTY_CHOICES,
                                default='Easy') 

    hint = models.TextField(blank=True)
    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')    

    def __str__(self):
        return self.name
    def summary(self):
        return self.body[:100]