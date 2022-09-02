from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Profile
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required

def registerUser(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('login')

    context= {'form':form}
    return render(request, 'user/register.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'user/login.html')

def logoutUser(request):
    logout(request)
    messages.info(request,'User was logged out!')
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