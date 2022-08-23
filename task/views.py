from django.shortcuts import render, redirect 
from .models import Task, Rezolutie, Label, Componenta
from .forms import TaskForm, ComponentaForm, RezolutieForm, LabelForm
from egm.models import Egm, Cabinet
from location.models import Location
import json



def dashboard(request):
    open = Task.objects.filter(status='open')
    closed = Task.objects.filter(status='closed')
    progres = Task.objects.filter(status='in_progres')
    vnet = Task.objects.filter(status='waiting_vnet')
    cmac = Task.objects.filter(status='waiting_cmac')
    lnm = Task.objects.filter(status='waiting_lnm')

    context = {'open':open,'closed':closed,'progres':progres,
        'vnet':vnet,'cmac':cmac,'lnm':lnm}
    return render(request, 'task/dashboard.html', context)



def tasks(request):
   
    componente = Componenta.objects.all()
    cabinete = Cabinet.objects.all()
    egms = Egm.objects.all()
    rezolutii = Rezolutie.objects.all()
    labels = Label.objects.all()
    tasks = Task.objects.all()
    locatii = Location.objects.all()
    context = {'tasks':tasks, 'rezolutii':rezolutii, 'labels':labels,
    'componente':componente, 'cabinete':cabinete, 'egms':egms, 'locatii':locatii}
    return render(request, 'task/tasks.html', context)



def task(request, pk):
    task = Task.objects.get(nr=pk)

    profile = request.user.profile
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('task',pk=task.nr )

    context = {'task':task, 'form':form}
    return render(request, 'task/task.html', context)


def edithTask(request, pk):
    locatii = Location.objects.all()
    egm = list(Egm.objects.values('id','serie','locatia_id'))
    task = Task.objects.get(nr=pk)

    profile = request.user.profile
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
        
            return redirect('task',pk=task.nr )

    context = {'task':task, 'form':form, 'listaJs':json.dumps(egm),'locatii':locatii}
    return render(request, 'task/task_form.html', context)



def taskFilter(request, pk):
    value = pk
    tasks = Task.objects.filter(status=value)
    print(request)

    context = {'tasks':tasks}
    return render(request, 'task/tasks.html', context)



def createTask(request):
    locatii = Location.objects.all()
    egm = list(Egm.objects.values('id','serie','locatia_id'))
    profile = request.user.profile
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            task = form.save()
            task.owner = profile
            task.save()
            return redirect('tasks')
        
    context = {'form': form, 'listaJs':json.dumps(egm),'locatii':locatii}
    return render(request, 'task/task_form.html', context)


def createComponenta(request):
    form = ComponentaForm()

    if request.method == 'POST':
        form = ComponentaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('tasks')

    context = {'form':form}
    return render(request, 'task/form.html', context)



def createRezolutie(request):
    form = RezolutieForm()

    if request.method == 'POST':
        form = RezolutieForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('tasks')

    context = {'form':form}
    return render(request, 'task/form.html', context)



def createLabel(request):
    form = LabelForm()

    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('tasks')

    context = {'form':form}
    return render(request, 'task/form.html', context)