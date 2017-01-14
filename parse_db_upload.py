import cPickle as cp
from .models import Recipe, Ingredient

with open('food_data','rb') as f:
	myDict = cp.load(f)

for i in range(len(myDict)):
	title = myDict[i]['title']
	cal = myDict[i]['calories']
	img_url = myDict[i]['image_url']
	rec_url = myDict[i]['recipe_url']
	rec = Recipe(title=title,calories=cal,image_url=img_url,recipe_url=rec_url)
	rec.save()
	for j in range(len(myDict[i]['ingredients'])):
		ing = Ingredient(ingredient = myDict[i]['ingredients'][j]['text'])
		ing.save()
		rec.ingredients.add(ing)