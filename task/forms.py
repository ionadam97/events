from django.forms import ModelForm, TextInput
from .models import Task, Componenta, Label, Rezolutie 


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['locatia', 'componenta', 'label', 'egm',
                  'informatorul', 'rezolutie', 'problema', 'solutie',
                  'sumar', 'responsabil' ,'status']

        widgets = {
            'locatia': TextInput(attrs={'list': 'locatie'}),
            'egm': TextInput(attrs={'list': 'adj'}),
            
         }
         
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})




class ComponentaForm(ModelForm):
    class Meta:
        model = Componenta
        fields = ['name']
        labels = {
            'name': 'Introduceti tipul de componenta',
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class LabelForm(ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        labels = {
            'name': 'Introduceti label',
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


class RezolutieForm(ModelForm):
    class Meta:
        model = Rezolutie
        fields = ['name']
        labels = {
            'name': 'Introduceti rezolutie',
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
        }


