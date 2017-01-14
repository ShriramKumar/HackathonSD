from django.db import models

# Create your models here.
class Ingredient(models.Model):
	ingredient = models.CharField(max_length=300)

	def __str__(self):
		return self.ingredient

class Recipe(models.Model):
	title = models.CharField(max_length=200)
	ingredients = models.ManyToManyField(Ingredient)
	calories = models.IntegerField()
	image_url = models.CharField(max_length=300)
	recipe_url = models.CharField(max_length=300)

	def __str__(self):
		return self.title

class UserInput(models.Model):
	input_search = models.ForeignKey(Recipe, null=False)