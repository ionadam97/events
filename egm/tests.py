from django.test import TestCase
from .models import Egm, Cabinet, Platform
from location.models import Location
import csv
# Create your tests here.

def open_csv():
    data = []
    with open('egm/cabinets.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ";")
        for rows in csv_reader:
            data.append(rows)
    return data
    


 
def creaza():
    data = open_csv()
    cabinets = Cabinet.objects.all()
    platforms = Platform.objects.all()
    locations = Location.objects.all()
    for egm in data:
        for cabinet in cabinets:
            print(cabinet.id)
            if egm['Cabinet'] == cabinet.name:
                egm['Cabinet'] = cabinet

        for location in locations:
            print(location.id)
            if egm['Outlet'] == location.numar:
                egm['Outlet'] = location
    
    for egm in data:
        
        if egm['Cabinet'] == cabinets[5] or egm['Cabinet'] == cabinets[4]:
            plat= platforms[0]
        else:
            plat= platforms[1]

        Egm.objects.create(serie=egm['ADJ'], cabinet= egm['Cabinet'],
          platforma=plat, locatia=egm['Outlet'])



    # egms =[{'serie':'123','cabinet':'FV624ACF2'},{'serie':'123','cabinet':'FV624ACF2'}]
    # platforms = Platform.objects.get(id=1)
    # locations = Location.objects.get(id=1)
    # cabinets = Cabinet.objects.all()
    # for egm in egms:
    #     for cabinet in cabinets:
    #         print(cabinet.id)
    #         if egm['cabinet'] == cabinet.name:
    #             egm['cabinet'] = cabinet
    # for egm in egms:
    #     print(egm)
    #     Egm.objects.create(serie=egm['serie'], cabinet= egm['cabinet'], platforma=platforms, locatia=locations)

