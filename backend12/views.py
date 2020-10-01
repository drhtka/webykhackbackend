# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from backend13.models import CreateDb
from django.shortcuts import render, redirect


class Backend12View(View):
    # выводим на страницу
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale')
        return render(request, 'backend12/backend12.html', {'all_goods': all_goods})

class Backend12OutView(View):
    # удаляем и выводим на страницу
    def post(self, request):
        print(request.POST.get('id'))
        CreateDb.objects.filter(id=request.POST.get('id')).update(sale=request.POST.get('valtext'))# удаляем
        todo_id = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale')
        return render(request, 'backend12/backend12.html', {'all_goods': todo_id})

        #return render(request, 'backend13/backend10.html', {'all_goods': my_return})