from django.shortcuts import render, redirect
from .forms import LocationForm, ManagerForm
from .models import Location, Manager
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def locations(request):
    locations = Location.objects.all()
    context = {'locations':locations}
    return render(request, 'location/locations.html', context)


@login_required(login_url='login')
def managers(request):
    managers = Manager.objects.all()
    context = {'managers':managers}
    return render(request, 'location/managers.html', context)


@login_required(login_url='login')
def createLocation(request):
    form = LocationForm()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('locations')
        
    context = {'form': form}
    return render(request, 'location/location_form.html', context)


@login_required(login_url='login')
def createManager(request):
    form = ManagerForm()
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('locations')
        
    context = {'form': form}
    return render(request, 'location/location_form.html', context)