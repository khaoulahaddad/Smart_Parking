from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from khaoulaApp.models import Place
from khaoulaApp.models import Reservation
from khaoulaApp.models import Facture
import json
import time
from datetime import datetime
from django.utils.timezone import get_current_timezone
from time import strftime
#from chronothread import Chrono

# Create your views here.
def home(request):
	return TemplateResponse(request, 'home.html',{})

#changer l'etat du Place (update)
def reserver(request, identif):
	p=Place.objects.get(id=identif)
	if(p.etat== 1):
		Place.objects.select_related().filter(id=identif).update(etat= 0)
		Reservation.objects.create(idPlace_id=identif,idCar_id=5, date_debut=str(datetime.now(tz=get_current_timezone())))
		#chrono =Chrono(identif)
		#chrono.start()
		
	else :
		Place.objects.select_related().filter(id=identif).update(etat=1)
		res=Reservation.objects.get(idPlace_id=identif, date_fin= None)
		Reservation.objects.filter(idPlace_id=identif, date_fin= None).update(date_fin=str(datetime.now(tz=get_current_timezone())))
	return HttpResponse("done")

def money(request, identif):
	datetimeFormat = '%Y/%m/%d %H:%M:%s:%f'
	res=Reservation.objects.get(id=identif)
	place={}
	date=res.date_fin - res.date_debut
	datetime = date.seconds
	hours=datetime/3600
	minutes = (datetime-hours*3600)/60
	seconds = datetime-hours*3600-minutes*60
	money = hours*1
	if (minutes !=0 | seconds !=0):
		money=money + 1
	place["money"]= money
	return HttpResponse(json.dumps(place))

def color(request, identif):
	p=Place.objects.get(id=identif)
	plist={}
	plist["etat"] = p.etat
	#plist["heur"] = p.heur
	#plist["minute"]= p.minute
	#plist["seconde"]= p.sec
    	return HttpResponse(json.dumps(plist))
