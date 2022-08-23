from django.shortcuts import render, redirect
from .forms import LocationForm, ManagerForm
from .models import Location
# Create your views here.
def locations(request):
    locations = Location.objects.all()

    context = {'locations':locations}
    return render(request, 'location/locations.html', context)


def createLocation(request):
    form = LocationForm()

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('locations')
        
    context = {'form': form}
    return render(request, 'location/location_form.html', context)


def createManager(request):
    form = ManagerForm()

    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('locations')
        
    context = {'form': form}
    return render(request, 'location/location_form.html', context)