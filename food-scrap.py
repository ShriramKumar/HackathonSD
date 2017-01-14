import random
import math
import urllib
import json
import csv
import cPickle as cp

dish_list = []

def retrieve(url):
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	global dish_list
	for a in data["hits"]:
		dish = {}
		dish['title'] = a["recipe"]["label"]
	  	dish['ingredients'] = a["recipe"]["ingredients"]
	  	dish['calories'] = a["recipe"]["calories"]
	  	dish['image_url'] = a["recipe"]["image"]
	  	dish['recipe_url'] = a["recipe"]["url"]
	  	dish_list.append(dish)
	
if __name__ == "__main__":
	with open('Ingredients.csv','r') as f:
		reader = csv.reader(f)
		ingredients = list(reader)
	
	for i,ingredient in enumerate(ingredients):
		first = "https://api.edamam.com/search?q="
		q = ingredient[0].replace('_',' ')
		second = "&app_id=380acd5c&app_key=5328bfa2149c7ce6013b011e6f050be5&from=0&to=10000"
		url = first + q + second
		try:			
			retrieve(url)
		except:
			print i
		finally:
			with open('food_data','wb') as f:
				if len(dish_list) > 0:
					cp.dump(dish_list,f)