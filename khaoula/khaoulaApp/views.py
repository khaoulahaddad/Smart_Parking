from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from khaoulaApp.models import Place
import json
import time
from chronothread import Chrono

# Create your views here.
def home(request):
	return TemplateResponse(request, 'home.html',{})
#changer l'etat du Place (update)
def reserver(request, identif):
	p=Place.objects.get(id=identif)
	place={}
	if(p.etat=='l'):
		Place.objects.select_related().filter(id=identif).update(etat='o')
		chrono =Chrono(identif)
		chrono.start()
	else :
		Place.objects.select_related().filter(id=identif).update(etat='l')
	return HttpResponse(json.dumps(place))

def money(request, identif):
	p1=Place.objects.get(id=identif)
	place={}
	place["etat"] = p1.etat
	place["heur"] = p1.heur
	place["minute"]= p1.minute
	place["seconde"]= p1.sec
	money=p1.heur*1
	if(p1.minute!=0 or p1.sec!=0):
		money=money+1
	place["money"]=money	
	return HttpResponse(json.dumps(place))

def color(request, identif):
	p=Place.objects.get(id=identif)
	plist={}
	plist["etat"] = p.etat
	plist["heur"] = p.heur
	plist["minute"]= p.minute
	plist["seconde"]= p.sec
    	return HttpResponse(json.dumps(plist))

def argent(request, identif):
	p=Place.objects.get(id=identif)
	h=p.heur
	m=p.minute
	s=p.sec
	#if(p.etat=='l'and ((h!=0) or (m!=0) or (s!=0))):
	Place.objects.select_related().filter(id=identif).update(heur=0)
	Place.objects.select_related().filter(id=identif).update(minute=0)
	Place.objects.select_related().filter(id=identif).update(sec=0)
	
	return HttpResponse("done")

