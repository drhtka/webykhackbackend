from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from backend19.models import CreateDb
from django.shortcuts import render, redirect

class Backend19View(View):
    # выводим товары на странице товаров
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')

        plus_th = []
        for todo_id_s in all_goods:

            tmp_l8st = todo_id_s[0] + 1000, todo_id_s[1], todo_id_s[2], todo_id_s[3], todo_id_s[4]
            plus_th.append(tmp_l8st)

        return render(request, 'backend19/backend19.html', {'all_goods': plus_th})

class Backend19OutView(View):
    # Админка
    def get(self, request):
        id= request.GET.get('i')
        name = request.GET.get('name')
        price= request.GET.get('price')
        sale = request.GET.get('sale')
        all_goods = id, name, price, sale
        return render(request, 'backend19/backendout19.html',  {'all_goods': all_goods})

