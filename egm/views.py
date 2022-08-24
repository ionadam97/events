from django.shortcuts import render, redirect
from .forms  import EgmForm, CabinetForm, PlatformForm
from location.models import Location
from .models import Egm, Cabinet, Platform
# Create your views here.
def egm(request):
    cabinete = Cabinet.objects.all()
    egms = Egm.objects.all()
    locatii = Location.objects.all()
    platforme = Platform.objects.all()

    context = {'cabinete':cabinete, 'egms':egms, 
                "locatii":locatii, 'platforme':platforme}
    return render(request, 'egm/egm.html', context)

def platform(request):
    platforme = Platform.objects.all()

    context = {'platforme':platforme}
    return render(request, 'egm/platforme.html', context)

def cabinet(request):
    cabinete = Cabinet.objects.all()

    context = {'cabinete':cabinete}
    return render(request, 'egm/cabinet.html', context)


def createEgm(request):
    form = EgmForm()
    value = 'egm'
    if request.method == 'POST':
        form = EgmForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('egm')
        
    context = {'form': form, 'value':value}
    return render(request, 'egm/egm_form.html', context)


def createCabinet(request):
    form = CabinetForm()
    value = 'cabinet'
    if request.method == 'POST':
        form = CabinetForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('cabinet')
        
    context = {'form': form,'value':value}
    return render(request, 'egm/egm_form.html', context)


def createPlatform(request):
    form = PlatformForm()
    value = 'platform'
    if request.method == 'POST':
        form = PlatformForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('platform')
        
    context = {'form': form, 'value':value}
    return render(request, 'egm/egm_form.html', context)



