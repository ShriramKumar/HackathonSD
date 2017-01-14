from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
#from foodSpyderSite.forms import *

from .models import Recipe, Ingredient, UserInput

@csrf_protect
def index(request):
	matched_recipes = []
	if request.method == 'POST':
		if 'inputRecipe' in request.POST:
			matched_recipes = ['bisibelebath']
	return render_to_response('index.html', {'matches':matched_recipes}, RequestContext(request))