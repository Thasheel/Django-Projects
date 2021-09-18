from django.shortcuts import render, redirect

from core.forms import Tudoform
from core.models import Tudo


def home(request):
    forms = Tudoform()
    tudo = Tudo.objects.all()
    if request.method == 'POST':
        form = Tudoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'home.html', {'form': forms, 'tudo': tudo})


def update(request, tudo_id):
    tudo = Tudo.objects.get(id=tudo_id)
    forms = Tudoform(instance=tudo)
    if request.method == "POST":
        form = Tudoform(request.POST, instance=tudo)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update.html', {'form': forms})


def delete(request, tudo_id):
    if request.method == "POST":
        Tudo.objects.get(id=tudo_id).delete()
        return redirect('home')
