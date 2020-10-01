# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from backend15.models import CreateDb
from django.shortcuts import render, redirect



class Backend15View(View):
    # выводим товары
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale')
        return render(request, 'backend15/backend15.html', {'all_goods': all_goods})

class Backend15OutView(View):
    # фильтруем товары
    def post(self, request):
        chekbox_filter = CreateDb.objects.filter(category=request.POST.get('cat')).values_list('id', 'tovarname', 'price', 'sale', 'category')
        return render(request, 'backend15/backendout15.html', {'chekbox_filter': chekbox_filter})




