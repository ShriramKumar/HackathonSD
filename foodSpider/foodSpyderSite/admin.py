from django.contrib import admin

# Register your models here.
from .models import Ingredient, Recipe, UserInput

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(UserInput)