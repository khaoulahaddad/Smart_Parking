# Create your models here.
from django.db import models

class Place(models.Model):
	etat = models.BooleanField()
	def __unicode__(self):
		return "{0} [{1}]".format(self.num, self.etat)

class Voiture(models.Model):
	matricule = models.CharField(max_length=15)
	def __unicode__(self):
		return "{0} [{1}]".format(self.num, self.matricule)

class Reservation(models.Model):
	idPlace = models.ForeignKey('Place')
	idCar = models.ForeignKey('Voiture')
	date_debut= models.DateTimeField(null=True)
	date_fin= models.DateTimeField(null=True)
	def __unicode__(self):
		return "{0} [{1}]".format(self.num,self.etat,self.idPlace.num,self.idCar.num,self.date_debut,self.date_fin)

class Facture(models.Model):
	idReservation = models.ForeignKey('Reservation')
	prix_total= models.IntegerField(null=True)
	def __unicode__(self):
		return "{0} [{1}]".format(self.num,self.idReservation.num,self.prix_total)