from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from . models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



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





def profiles(request):
   
    profiles = Profile.objects.all

    context = {'profiles': profiles}
    return render(request, 'user/profiles.html', context)


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



    context = {}
    return render(request, 'user/profile_form.html', context)