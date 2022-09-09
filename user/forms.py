from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, FileInput
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        model._meta.get_field('email')._unique = True
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nume', 'prenume', 'email', 'location', 'url_facebook',
                  'phone', 'phone_serviciu', 'functie', 'profile_image']
        widgets = {
            'profile_image': FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
