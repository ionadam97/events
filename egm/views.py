from django.shortcuts import render, redirect
from .forms  import EgmForm, CabinetForm, PlatformForm
# Create your views here.
def egm(request):
    context = {}

    return render(request, 'egm/egm.html', context)


def createEgm(request):
    form = EgmForm()

    if request.method == 'POST':
        form = EgmForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('egm')
        
    context = {'form': form}
    return render(request, 'egm/egm_form.html', context)


def createCabinet(request):
    form = CabinetForm()

    if request.method == 'POST':
        form = CabinetForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('egm')
        
    context = {'form': form}
    return render(request, 'egm/egm_form.html', context)


def createPlatform(request):
    form = PlatformForm()

    if request.method == 'POST':
        form = PlatformForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('egm')
        
    context = {'form': form}
    return render(request, 'egm/egm_form.html', context)



