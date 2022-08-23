from logging import PlaceHolder
from django.forms import ModelForm
from .models import  Location, Manager
from django import forms


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['numar','name','address','telefon','adresa_ip',
            'manager', 'data_deschidere','data_inchidere', 'status']
        labels = {
            'numar': 'Introduceti numarul locatiei',
            'name': 'Introduceti numele locatiei',
        }
        
    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ['nume','email','telefon']
        labels = {
            'email': 'Introduceti email',
            'nume': 'Introduceti numele ',
            'telefon': 'Introduceti numarul de telefon',
        }
        
    def __init__(self, *args, **kwargs):
        super(ManagerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})