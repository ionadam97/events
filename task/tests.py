from django.test import TestCase
from egm.models import Egm
from .models import Task, Componenta, Label, Rezolutie
from location.models import Location
# Create your tests here.
def creaza_task():
    i = 0
    y = 0
    egms = Egm.objects.all()
    locations = Location.objects.all()
    inform = ['Caragia Maria ', 'Flora Ina', 'Alexandru Marian', 'Igor Spinu']
    owners = ['Aion ', 'Pradu', 'Vdanu', 'Cvalentin']
    respon = [ 'Vdanu', 'Aion ', 'Cvalentin','Pradu',]
    problem = ['monitorul nu afiseaza imaginea','nu functioneaza butonul start', 
                'sa blocat cardul in adj', 'Adj-ul emite zgomote ciudate']
    solutii = ['restart de la distanta','se va deplasa un tehnician',
                'Adj-ul a fost deconectat', 'remote restart, trebuie monitorizat ']
    statusuri = [ 'open', 'closed','in_progres', 'waiting_vnet','waiting_cmac','waiting_lnm']
    componente = Componenta.objects.all()
    labels = Label.objects.all()
    rezolutii = Rezolutie.objects.all()
   
    for location in locations:
        for egm in egms:
            if location.id == egm.locatia.id:
                i = i+1
                if y<3:
                    y = y+1
                else:
                    y=0

                if i <25 :
                    Task.objects.create(locatia=location, egm= egm,owner= owners[y], informatorul= inform[y], 
                    problema= problem[y], solutie = solutii[y], componenta=componente[y], label=labels[y], 
                    rezolutie= rezolutii[y], status= statusuri[y], responsabil = respon[y])
                