from threading import Thread
import time
from khaoulaApp.models import Place

class Chrono (Thread):
	def __init__(self, identif):
		Thread.__init__(self)
		self.identif = identif
		self.s=0
		self.m=0
		self.h=0
		
	def run(self):
		while(1):
			p=Place.objects.get(id=self.identif)
			if (p.etat=='l'):
				break
			self.s=self.s+1
			if (self.s==60):
				self.s=0
				self.m=self.m+1
			if (self.m==60):
				self.m=0
				self.h=self.h+1
			time.sleep(1)
			print "a"
			Place.objects.select_related().filter(id=self.identif).update(heur=self.h)
			Place.objects.select_related().filter(id=self.identif).update(minute=self.m)
			Place.objects.select_related().filter(id=self.identif).update(sec=self.s)

