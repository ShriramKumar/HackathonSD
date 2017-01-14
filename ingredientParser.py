import re

class ingredientParser:
	checker_list = []

	def __init__(self, ingre_list):
		for a in ingre_list:
			a = a.replace('_', ' ')
			self.checker_list.append(a)
		self.checker_list.sort(key = len, reverse=True)

	def search_string(self, check_str):
		parts = check_str.split(" ")
		for entry in self.checker_list:
			for part in parts:
				if entry.find(part) != -1:
					return entry.replace(' ', '_')
		return None

	def __repr__(self):
		return str(self.checker_list)	


