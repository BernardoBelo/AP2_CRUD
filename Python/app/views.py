from django.shortcuts import redirect, render
from app.forms import MotosForm
from app.models import Motos

# Create your views here.

def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Motos.objects.filter(marca__icontains=search)
    else:
        data['db'] = Motos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = MotosForm()
    return render(request, 'form.html', data)

def create(request):
    form = MotosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    data['form'] = MotosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    form = MotosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Motos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def sell(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    data['form'] = MotosForm(instance=data['db'])
    return render(request, 'sell.html', data)

def sellconfirm(request, pk):
    data = {}
    data['db'] = Motos.objects.get(pk=pk)
    history = MotosForm(request.POST or None, instance=data['db'])
    if history.is_valid():
        history.save('history.html')
        return redirect('home')

def history(request):
    history = {}
    history[sellconfirm] = request.GET.get(request.GET or None)
    return render(request, 'history.html', history)