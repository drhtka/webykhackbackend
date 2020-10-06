from django.views.generic.base import View
from backend16.models import CreateDb
from django.shortcuts import render, redirect

class Backend16View(View):
    # выводим товары
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')
        return render(request, 'backend16/backend16.html', {'all_goods': all_goods})


class Backend16OutView(View):
    def post(self, request):
        price_start = 0
        price_end = 999
        if request.POST.get('mini') != '':
            price_start = request.POST.get('mini')
        if request.POST.get('maxi') != '':
            price_end = request.POST.get('maxi')

        all_goods = CreateDb.objects.filter(price__gte=price_start).filter(price__lte=price_end).values_list('id', 'tovarname', 'price', 'sale', 'category')

        return render(request, 'backend16/backendout16.html', {'all_goods': all_goods})