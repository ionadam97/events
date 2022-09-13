from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, FileInput, forms
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if email.endswith('@novoinvestment.md'):
            try:
                user = User.objects.get(email=email)
            except Exception as e:
                return email
            raise forms.ValidationError(f"Email-ul {email} este folosit deja.")
            
        else:
            raise forms.ValidationError(f"Email-ul {email} nu este valid, email-ul trebuie sa se finalizeze cu @novoinvestment.md.")


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(f"Username: {username} este folosit deja.")


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
