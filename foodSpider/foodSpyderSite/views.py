from django.http import HttpResponse

def index(request):
	return HttpResponse("Food Spyder is up!!")

# Create your views here.
