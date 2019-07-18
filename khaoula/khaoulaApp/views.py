from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template.response import TemplateResponse
from khaoulaApp.models import Place
from khaoulaApp.models import Reservation
from khaoulaApp.models import Facture
from khaoulaApp.models import Voiture
from khaoulaApp.models import Etage
import json
import time
from datetime import datetime
from django.http import HttpResponseRedirect
from django.utils.timezone import get_current_timezone
from time import strftime
from django.shortcuts import redirect

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
	response = HttpResponseRedirect('/home')
#verification avec openCv True
	if(not Voiture.objects.filter(matricule_gauche=matri_gauche, matricule_droite=matri_droite)):
		Voiture.objects.create(matricule_gauche=matri_gauche, matricule_droite=matri_droite)
	return HttpResponseRedirect('/home')
#else:
	##if(not(request.COOKIES.get('Your_Cookies'))):
		##return HttpResponseRedirect('/')
	##else:
		##return HttpResponseRedirect('/home')

def home(request):
	my_car = request.session.get('my_car')
	print(my_car)
	if (not(my_car)):
		return HttpResponseRedirect('/')
	else :
		#App:reserver_par_etage

		return TemplateResponse(request, 'home.html',{})

def reserver_par_Etage(request):
	if(not(request.COOKIES.get('Your_Cookies'))):#vide
		response= HttpResponse(json.dumps(resultat))
		#degager id voiture:
		voiture_num=Voiture.objects.get(matricule_gauche=matri_gauche, matricule_droite=matri_droite).id
		response.set_cookie('Your_Cookies', voiture_num)
		resultat_etage=True
		numetage=1
		last_id_etage=Eatge.objects.last().id
		while ((resultat_etage==True) && (numetage <= last_id_etage)):
			resultat_place=False
			numplace=1
			last_id_place=Place.objects.filter(idEtage_id=numetage).last().id
			while((resultat_place==False) && (numplace <= last_id_place)):
				p=Place.objects.get(id=numplace)
				if (p.etat==0):
					resultat_place=True
				else :
					numplace=num+1
			if(resultat_place==True):
				resultat_etage=False
			else:
				numetage=numetage+1
		if (resultat_etage==False):
			Place.objects.filter(id=numplace, idEtage_id=numetage).update(etat=1)
			Reservation.objects.create(idPlace_id=numplace,idCar_id=,voiture_num, date_debut=str(datetime.now(tz=get_current_timezone())))
			return HttpResponse("done")
		else:
			return HttpResponse("complet")
	else:
		return HttpResponse("deja reserver")

#mezelet
def money(request):
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
	place["money"]=money
	response=HttpResponse(json.dumps(place))
	del request.session['my_car']
	response.delete_cookie('Your_Cookies')
	return response