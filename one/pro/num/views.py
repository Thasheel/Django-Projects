# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from num.models import phone


def my_view(request):
    user_phone=User.objects.get(id=1).phone#simple relation tget a phone number
    print(user_phone)
    #pho=phone.objects.get(user_id=user.id)


    user=phone.objects.get(id=1).user_id#to get a user name
    print(user)
