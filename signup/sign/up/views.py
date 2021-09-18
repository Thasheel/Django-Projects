# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse


# Create your views here.
from up.form import CustomUserCreationForm


def register_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("Register successfully")
            return redirect(reverse('register'))
    return render(request, 'reg.html', {'form': form})
