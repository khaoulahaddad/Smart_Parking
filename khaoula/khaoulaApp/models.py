# Create your models here.
from django.db import models

class Place(models.Model):
	etat = models.CharField(max_length=1)
	heur = models.IntegerField(default=0)
	minute = models.IntegerField(default=0)
	sec = models.IntegerField(default=0)
	def __unicode__(self):
		return "{0} [{1}]".format(self.num, self.etat)
