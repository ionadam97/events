from django.test import TestCase
from egm.models import Egm
from .models import Task
from location.models import Location
# Create your tests here.
def creaza_task():
    i = 0
    egms = Egm.objects.all()
    locations = Location.objects.all()

    for location in locations:
        for egm in egms:
            if location.id == egm.locatia.id:
                i = i+1
                if i <50:
                    Task.objects.create(locatia=location, egm= egm, problema= 'nu functioneaza butonul start', solutie = 'se va deplasa un tehnician')