from django.db import models
from ingredients.models import Ingredient
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')    

    def __str__(self):
        return self.name
    def summary(self):
        return self.body[:100]