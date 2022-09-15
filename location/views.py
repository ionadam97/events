from django.shortcuts import render, redirect
from .forms import LocationForm, ManagerForm
from .models import Location, Manager
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.



def locations(request):
    locations = Location.objects.all()
    
    context = {'locations': locations}
    return render(request, 'location/locations.html', context)



def managers(request):
    managers = Manager.objects.all()

    context = {'managers': managers}
    return render(request, 'location/managers.html', context)

@permission_required('is_staff')
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

@permission_required('is_staff')
@login_required(login_url='login')
def createManager(request):
    form = ManagerForm()
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('managers')

    context = {'form': form}
    return render(request, 'location/location_form.html', context)

@permission_required('is_staff')
@login_required(login_url='login')
def edithLocation(request, pk):
    locatia = Location.objects.get(id=pk)
    form = LocationForm(instance=locatia)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=locatia)
        if form.is_valid:
            form.save()
            return redirect('locations')

    context = {'form': form}
    return render(request, 'location/location_form.html', context)

@permission_required('is_staff')
@login_required(login_url='login')
def edithManager(request, pk):
    manager = Manager.objects.get(id=pk)
    form = ManagerForm(instance=manager)
    if request.method == 'POST':
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid:
            form.save()
            return redirect('managers')

    context = {'form': form}
    return render(request, 'location/location_form.html', context)

@permission_required('is_staff')
@login_required(login_url='login')
def deleteManager(request, pk):
    manager = Manager.objects.get(id=pk)
    if request.method == 'POST':
        manager.delete()
        return redirect('managers')

    context = {'object': manager}
    return render(request, 'delete_template.html', context)
