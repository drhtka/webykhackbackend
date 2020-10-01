# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from backend14.models import CreateDb
from django.shortcuts import render, redirect


class Backend14View(View):
    # выводим товары
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale')
        return render(request, 'backend14/backend14.html', {'all_goods': all_goods})

class Backend14OutView(View):
    def post(self, request):
        name_search = request.POST.get('name')
        name_filter = CreateDb.objects.filter(tovarname=name_search).values_list('id', 'tovarname', 'price', 'sale')
        print(len(name_filter))
        if len(name_filter) != 0:
            return render(request, 'backend14/backendout14.html', {'name_filter': name_filter})
        else:
            return render(request, 'backend14/backenderror14.html')





        #if name_filter == []:
        #    print('hello')
        #else:
        #