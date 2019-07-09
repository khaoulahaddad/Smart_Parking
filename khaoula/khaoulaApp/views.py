from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from khaoulaApp.models import Place
from khaoulaApp.models import Reservation
from khaoulaApp.models import Facture
from khaoulaApp.models import Voiture
import json
import time
from datetime import datetime
from django.utils.timezone import get_current_timezone
from time import strftime
#from chronothread import Chrono

# Create your views here.
#def login(request):
#	Reservation.objects.create(matricule = identif)
#	return TemplateResponse(request, 'login.html',{})

def home(request):
	return TemplateResponse(request, 'home.html',{})

#changer l'etat du Place (update)
def reserver(request, identif):
	datetimeFormat = '%Y/%m/%d %H:%M:%s:%f'
	p=Place.objects.get(id=identif)
	if(p.etat== 1):
		#voiture = Voiture.objects.last()
		Place.objects.select_related().filter(id=identif).update(etat= 0)
		Reservation.objects.create(idPlace_id=identif,idCar_id=5, date_debut=str(datetime.now(tz=get_current_timezone())))
		#chrono =Chrono(identif)
		#chrono.start()
		
	else :
		Place.objects.select_related().filter(id=identif).update(etat=1)
		res=Reservation.objects.get(idPlace_id=identif, date_fin= None).id
		Facture.objects.create(idReservation_id=(Reservation.objects.get(idPlace_id=identif, date_fin= None).id))
		Reservation.objects.filter(idPlace_id=identif, date_fin= None).update(date_fin=str(datetime.now(tz=get_current_timezone())))
		date=Reservation.objects.get(id=res).date_fin - Reservation.objects.get(id=res).date_debut
		datesec = date.seconds
		hours=datesec/3600
		minutes = (datesec-hours*3600)/60
		seconds = datesec-hours*3600-minutes*60
		money = hours*1
		if (minutes !=0 | seconds !=0):
			money=money + 1	
		Facture.objects.filter(idReservation_id=res).update(prix_total=money)
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

def idplace (request):
	plist={}
	i=0
	for p in Place.objects.all():
		obj={}
		obj["idplace"]= p.id
		obj["etat"]= p.etat
		plist[i]=obj
		i=i+1
	return HttpResponse(json.dumps(plist))
