from django.test import TestCase
from egm.models import Egm
from .models import Task, Componenta, Label, Rezolutie
from location.models import Location
# Create your tests here.
def creaza_task():
    i = 0
    egms = Egm.objects.all()
    locations = Location.objects.all()
    inform = ['Caragia Maria ', 'Flora Ina', 'Alexandru Marian', 'Igor Spinu']

    for location in locations:
        for egm in egms:
            if location.id == egm.locatia.id:
                i = i+1
                inf = i%3
                if i <30 and i%2==0:
                    Task.objects.create(locatia=location, egm= egm, informator= inform[inf], componenta = '',
                     problema= 'nu functioneaza butonul start', solutie = 'se va deplasa un tehnician')
                