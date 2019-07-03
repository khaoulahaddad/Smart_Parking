from django.contrib import admin
from khaoulaApp.models import Place
from khaoulaApp.models import Voiture
from khaoulaApp.models import Reservation
from khaoulaApp.models import Facture

# Register your models here.
admin.site.register(Place)
admin.site.register(Reservation)
admin.site.register(Facture)
admin.site.register(Voiture)
