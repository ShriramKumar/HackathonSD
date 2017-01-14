import random
import math
import urllib
import json

def retrive(url):
  response = urllib.urlopen(url)
  data = json.loads(response.read())
  for a in data["hits"]:
  	print a
  	print "\n\n"


if __name__ == "__main__":
	ingredients = []
	'''
	for a in ingredients:
		first = "https://api.edamam.com/search?q=" 
		q = ""
		second = "&app_id=380acd5c&app_key=5328bfa2149c7ce6013b011e6f050be5&from=0&to=10000"

		url = first + q + second			
		retrive(url)
	'''
	first = "https://api.edamam.com/search?q=" 
	q = 
	second = "&app_id=380acd5c&app_key=5328bfa2149c7ce6013b011e6f050be5&from=0&to=10000"

	url = first + q + second			
	retrive(url)
