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
from khaoulaApp.models import Test
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

	if(not(request.COOKIES.get('Your_Cookies'))):
		voiture = Test.objects.order_by('id').last()
		if((matri_gauche == voiture.matricule_gauche) & (matri_droite == voiture.matricule_droite)):
			if(not Voiture.objects.filter(matricule_gauche=matri_gauche, matricule_droite=matri_droite)):
				Voiture.objects.create(matricule_gauche=matri_gauche, matricule_droite=matri_droite)
			voiture_num=Voiture.objects.get(matricule_gauche=matri_gauche, matricule_droite=matri_droite).id
			response.set_cookie('Your_Cookies', voiture_num)
			return response
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/home')

def home(request):
	my_car = request.session.get('my_car')
	if (not(my_car)):
		return HttpResponseRedirect('/')
	else :
		resultat={}
		voiture_num=int(request.COOKIES.get('Your_Cookies'))
		matri_gauche=Voiture.objects.get(id=voiture_num).matricule_gauche
		matri_droite =Voiture.objects.get(id=voiture_num).matricule_droite
		resultat["matricule_gauche"]= matri_gauche
		resultat["matricule_droite"]=matri_droite
		if(not(Reservation.objects.filter(idCar_id=voiture_num, date_fin=None))):
			resultat_etage=True
			numetage=0
			last_id_etage=Etage.objects.order_by('id').last().id
			while ((resultat_etage==True) & (numetage <= last_id_etage)):
				resultat_place=False
				last_place = Place.objects.filter(idEtage_id=numetage).order_by('id').last().id
				numplace = Place.objects.filter(idEtage_id=numetage).order_by('id').first().id
				#print(last_id_place.id)
				while((resultat_place==False) & (numplace <=last_place )):
					p=Place.objects.get(id=numplace)
					if (p.etat==0):
						resultat_place=True
					else :
						numplace=numplace+1
				if(resultat_place==True):
					resultat_etage=False
				else:
					numetage=numetage+1
			if (resultat_etage==False):
				Place.objects.filter(id=numplace, idEtage_id=numetage).update(etat=1)
				Reservation.objects.create(idPlace_id=numplace, idCar_id=voiture_num, date_debut=str(datetime.now(tz=get_current_timezone())))
				resultat["numero_etage"]=numetage
				resultat["numero_palce"]=Place.objects.get(id=numplace, idEtage_id=numetage).numero
				resultat["date_debut"]=Reservation.objects.get(idPlace_id=numplace, idCar_id=voiture_num, date_fin=None).date_debut
				return TemplateResponse(request, 'home.html',resultat)
			else:
				return HttpResponse("complet")	
		else:
			idplace=Reservation.objects.get(idCar_id=voiture_num, date_fin=None).idPlace_id
			resultat["numero_etage"]=Place.objects.get(id=idplace).idEtage_id
			resultat["numero_palce"]=Place.objects.get(id=idplace).numero
			resultat["date_debut"]=Reservation.objects.get(idPlace_id=idplace, idCar_id=voiture_num, date_fin=None).date_debut
			return TemplateResponse(request, 'home.html',resultat)
		#print((Res action="/money" method="POST"ervation.objects.get(idCar_id=voiture_num, date_fin = None).id)
		return HttpResponse("done")
		

def money(request):
	voiture_num=int(request.COOKIES.get('Your_Cookies'))
	res=Reservation.objects.get(idCar_id=voiture_num, date_fin=None)
	Place.objects.select_related().filter(id=res.idPlace_id).update(etat=0)
	Facture.objects.create(idReservation_id=(Reservation.objects.get(idPlace_id=res.idPlace_id, date_fin= None).id))
	Reservation.objects.filter(idPlace_id=res.idPlace_id, date_fin= None).update(date_fin=str(datetime.now(tz=get_current_timezone())))
	date=Reservation.objects.get(id=res.id).date_fin - Reservation.objects.get(id=res.id).date_debut
	place={}
	money=date.days*10 #prix de 24h = 10Dt
	datesec = date.seconds
	hours=datesec/3600
	minutes = (datesec-hours*3600)/60
	seconds = datesec-hours*3600-minutes*60
	money = money + hours*1 #prix 1Dt
	if (minutes !=0 | seconds !=0):
		money=money + 1	
	Facture.objects.filter(idReservation_id=res.id).update(prix_total=money)
	place["money"]=money
	response=HttpResponse(json.dumps(place))
	del request.session['my_car']
	response.delete_cookie('Your_Cookies')
	return response
	