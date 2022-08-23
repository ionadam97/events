from django.forms import ModelForm
from .models import Egm, Cabinet, Platform, Location
from django import forms


class EgmForm(ModelForm):
    class Meta:
        model = Egm
        fields = ['serie', 'cabinet', 'platforma', 'locatia']
        labels = {
            'serie': 'Introduceti seria ADJ-ului',
            'cabinet': 'Selectati tipul de cabinet'
        }

    def __init__(self, *args, **kwargs):
        super(EgmForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
        

class CabinetForm(ModelForm):
    class Meta:
        model = Cabinet
        fields = ['name']
        labels = {
            'name': 'Introduceti tipul de cabinet',
        }

    def __init__(self, *args, **kwargs):
        super(CabinetForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = ['name']
        labels = {
            'name': 'Introduceti tipul platformei',
        }

    def __init__(self, *args, **kwargs):
        super(PlatformForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name']
        labels = {
            'name': 'Introduceti locatia',
        }

    def __init__(self, *args, **kwargs):
        super(LocationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})