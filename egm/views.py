from calendar import c
from django.shortcuts import render, redirect
from .forms  import EgmForm, CabinetForm, PlatformForm
from location.models import Location
from .models import Egm, Cabinet, Platform
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required(login_url='login')
def egm(request):
    cabinete = Cabinet.objects.all()
    egms = Egm.objects.all()
    locatii = Location.objects.all()
    platforme = Platform.objects.all()

    context = {'cabinete':cabinete, 'egms':egms, 
                "locatii":locatii, 'platforme':platforme}
    return render(request, 'egm/egm.html', context)


@login_required(login_url='login')
def platform(request):
    platforme = Platform.objects.all()
    context = {'platforme':platforme}
    return render(request, 'egm/platforme.html', context)


@login_required(login_url='login')
def cabinet(request):
    cabinete = Cabinet.objects.all()
    context = {'cabinete':cabinete}
    return render(request, 'egm/cabinet.html', context)

@permission_required('is_staff')
@login_required(login_url='login')
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
@permission_required('is_staff')
@login_required(login_url='login')
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


@permission_required('is_staff')
@login_required(login_url='login')
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


@permission_required('is_staff')
@login_required(login_url='login')
def edithEgm(request, pk):
    egm = Egm.objects.get(id=pk)
    form = EgmForm(instance=egm)
    if request.method == 'POST':
        form = EgmForm(request.POST, instance=egm)
        if form.is_valid:
            form.save()
            return redirect('egm')
        
    context = {'form': form}
    return render(request, 'egm/egm_form.html', context)


@permission_required('is_staff')
@login_required(login_url='login')
def edithCabinet(request, pk):
    cabinet = Cabinet.objects.get(id=pk)
    form = CabinetForm(instance=cabinet)
    if request.method == 'POST':
        form = CabinetForm(request.POST, instance=cabinet)
        if form.is_valid:
            form.save()
            return redirect('cabinet')
        
    context = {'form': form}
    return render(request, 'egm/egm_form.html', context)


@permission_required('is_staff')
@login_required(login_url='login')
def edithPlatform(request, pk):
    platform = Platform.objects.get(id=pk)
    form = PlatformForm(instance=platform)
    if request.method == 'POST':
        form = PlatformForm(request.POST, instance=platform)
        if form.is_valid:
            form.save()
            return redirect('platform')
        
    context = {'form': form}
    return render(request, 'egm/egm_form.html', context)
