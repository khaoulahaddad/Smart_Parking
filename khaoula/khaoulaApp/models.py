# Create your models here.
from django.db import models

class Etage(models.Model):
	def __unicode__(self):
		return "{0} [{1}]".format(self.num)

class Place(models.Model):
	numero=models.IntegerField(null=True)
	etat = models.BooleanField()
	idEtage = models.ForeignKey('Etage')
	class Meta:
		unique_together = (('numero', 'idEtage'),)
	def __unicode__(self):
		return "{0} [{1}]".format(self.num,self.numero, self.etat, self.idEtage.num)

class Voiture(models.Model):
	matricule_gauche = models.CharField(max_length=3,null=True)
	matricule_droite = models.CharField(max_length=4,null=True)
	def __unicode__(self):
		return "{0} [{1}]".format(self.num,self.matricule_gauche, self.matricule_droite)

class Reservation(models.Model):
	idPlace = models.ForeignKey('Place')
	idCar = models.ForeignKey('Voiture')
	date_debut= models.DateTimeField(null=True)
	date_fin= models.DateTimeField(null=True)
	def __unicode__(self):
		return "{0} [{1}]".format(self.num,self.idPlace.num,self.idCar.num,self.date_debut,self.date_fin)

class Facture(models.Model):
	idReservation = models.ForeignKey('Reservation')
	prix_total= models.IntegerField(null=True)
	def __unicode__(self):
		return "{0} [{1}]".format(self.num,self.idReservation.num,self.prix_total)