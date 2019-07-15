from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.response import TemplateResponse
from khaoulaApp.models import Place
from khaoulaApp.models import Reservation
from khaoulaApp.models import Facture
from khaoulaApp.models import Voiture
import json
import time
from datetime import datetime
from django.http import HttpResponseRedirect
from django.utils.timezone import get_current_timezone
from time import strftime
from django.shortcuts import redirect
#from chronothread import Chrono

# Create your views here.
#def login(request):
#	Reservation.objects.create(matricule = identif)
#	return TemplateResponse(request, 'login.html',{})
class LoginView(TemplateView):

  template_name = 'front/login.html'

  def post(self, request, **kwargs):

    matri_gauche = request.POST.get('matricule_gauche', False)
    matri_droite = request.POST.get('matricule_droite', False)
    return render(request, self.template_name)

def login(request):
	matri_gauche = request.POST.get('matricule_gauche',False)
	matri_droite = request.POST.get('matricule_droite',False)
	request.session['my_car']=str(matri_gauche)+str(matri_droite)
	#print(request.session['my_car'])
	#verification avec openCv
	if(not Voiture.objects.filter(matricule_gauche=matri_gauche, matricule_droite=matri_droite)):
		Voiture.objects.create(matricule_gauche=matri_gauche, matricule_droite=matri_droite)
	voiture_num=Voiture.objects.get(matricule_gauche=matri_gauche, matricule_droite=matri_droite).id
	response = HttpResponseRedirect('/home')
	response.set_cookie('Your_Cookies', voiture_num)
	return response


def home(request):
	my_car = request.session.get('my_car')
	print(my_car)
	if (not(my_car)):
		return HttpResponseRedirect('/')
	else :
		print("ok")
		return TemplateResponse(request, 'home.html',{})

#changer l'etat du Place (update)
def reserver(request, identif):
	datetimeFormat = '%Y/%m/%d %H:%M:%s:%f'
	p=Place.objects.get(id=identif)
	place={}
	cookie_idCar=int(request.COOKIES.get('Your_Cookies'))
	if(p.etat== 0):
		if(not(Reservation.objects.filter(idCar_id=cookie_idCar,date_fin=None))):
			Place.objects.select_related().filter(id=identif).update(etat= 1)
			Reservation.objects.create(idPlace_id=identif,idCar_id=cookie_idCar, date_debut=str(datetime.now(tz=get_current_timezone())))
			place["etat"]=0
		else:
			place["etat"]=2
		return HttpResponse(json.dumps(place))
		#chrono =Chrono(identif)
		#chrono.start()
		
	else :
		idcar=Reservation.objects.get(idPlace_id=identif, date_fin= None).idCar_id
		if(int(request.COOKIES.get('Your_Cookies'))== idcar):
			place["etat"]=1
			Place.objects.select_related().filter(id=identif).update(etat=0)
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
			response=HttpResponse(json.dumps(place))
			del request.session['my_car']
			print("ok")
			response.delete_cookie('Your_Cookies')
			return response
		else:
			place["etat"]=2
			return HttpResponse(json.dumps(place))
	#return HttpResponse(json.dumps(place))

#def deletecookies(request):
#	response = HttpResponse("done")
#    response.delete_cookie("Your_Cookies")
#    return response

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
