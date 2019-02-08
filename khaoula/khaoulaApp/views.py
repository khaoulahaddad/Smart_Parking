from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
	return TemplateResponse(request, 'home.html',{})
def reserver(request, identif):
	#changer l'etat du Place (update)
	return HttpResponse("done")
