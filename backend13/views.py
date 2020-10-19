# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from backend13.models import CreateDb
from django.shortcuts import render, redirect


class Backend13View(View):
    # выводим на страницу
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale')
        return render(request, 'backend13/backend13.html', {'all_goods': all_goods})

class Backend13OutView(View):
    # удаляем и выводим на страницу
    def post(self, request):
        print(request.POST.get('id'))
        CreateDb.objects.filter(id=request.POST.get('id')).delete()# удаляем
        todo_id = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale')
        return render(request, 'backend13/backend13.html', {'all_goods': todo_id})

        #return render(request, 'backend13/backend10.html', {'all_goods': my_return})

class BackCreateProd13(View):
    def post(self, request):
        print(request.POST.get('name'))
        print(request.POST.get('price'))
        print(request.POST.get('sale'))
        #if request.POST.get('name') != 0 and request.POST.get('price') != 0 and request.POST.get('sale') !=0:
        seve_site = CreateDb(tovarname=request.POST.get('name'), price=request.POST.get('price'), sale=request.POST.get('sale'))
        seve_site.save()
        #all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale')
        #return render(request, 'backend13/backend13.html', {'all_goods': all_goods})
        return redirect('/backend13/')