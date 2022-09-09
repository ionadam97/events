from django.forms import ModelForm, TextInput
from .models import Egm, Cabinet, Platform


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
            field.widget.attrs.update({'class': 'form-control'})


class CabinetForm(ModelForm):
    class Meta:
        model = Cabinet
        fields = ['name']
        labels = {
            'name': 'Introduceti tipul de cabinet',
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = ['name']
        labels = {
            'name': 'Introduceti tipul platformei',
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }
