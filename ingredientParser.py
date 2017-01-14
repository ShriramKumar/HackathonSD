#!/usr/bin/python
import re

class ingredientParser:
   checker_list = []

   def __init__(self, ingre_list):
      for a in ingre_list:
      	a = a.replace('_', ' ')
      	self.checker_list.append(a)
      self.checker_list.sort(key = len, reverse=True)
   
   def search_string(self, check_str):
   	  for entry in self.checker_list:
   	  	if entry.find(check_str) != -1:
   	  		return entry.replace(' ', '_')
	  return None

   def __repr__(self):
      return str(self.checker_list)	

    