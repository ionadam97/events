from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Profile
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import account_activation_token


def registerUser(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            to_email = form.cleaned_data.get('email')
            if to_email.endswith('@novoinvestment.md'):
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.is_active = False
                user.save()

                # to get the domain of the current site  
                current_site = get_current_site(request)  
                mail_subject = 'Linkul de activare a fost trimis la ID-ul tău de e-mail'  
                message = render_to_string('acc_active_email.html', {  
                    'user': user,  
                    'domain': current_site.domain,  
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                    'token':account_activation_token.make_token(user),  
                })  
                
                email = EmailMessage(  
                            mail_subject, message, to=[to_email]  
                )  
                email.send()  
                return HttpResponse('Vă rugăm să vă confirmați adresa de e-mail pentru a finaliza înregistrarea')

                # login(request, user)
                # return redirect('login')

    context= {'form':form}
    return render(request, 'user/register.html', context)


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return HttpResponse('Vă mulțumim pentru confirmarea prin e-mail. Acum vă puteți autentifica contul.')  
    else:  
        return HttpResponse('Linkul de activare este nevalid!')  


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('account')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Numele de utilizator nu există')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request, 'Numele de utilizator sau Parola sunt incorecte')

    return render(request, 'user/login.html')

def logoutUser(request):
    logout(request)
    messages.warning(request,'Utilizatorul a fost deconectat!')
    return redirect('login')


@login_required(login_url='login')
def profiles(request):
    profiles = Profile.objects.all
    context = {'profiles': profiles}
    return render(request, 'user/profiles.html', context)

@login_required(login_url='login')
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'user/user_profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'user/account.html', context)


@login_required(login_url='login')
def edithAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save() 

            return redirect('account')


    context = {'form': form}
    return render(request, 'user/profile_form.html', context)