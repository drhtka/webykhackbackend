from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from backend18.models import CreateDb18
from django.shortcuts import render, redirect

class Backend18View(View):
    # выводим товары на странице товаров
    def get(self, request):
        all_goods = CreateDb18.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')
        print('all_goods-18')
        print(all_goods)
        return render(request, 'backend18/backend18.html', {'all_goods': all_goods})

class Backend18OutView(View):
    # Админка
    def get(self, request):
        all_goods = CreateDb18.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')
        print('all_goods-18')
        print(all_goods)
        return render(request, 'backend18/backendout18.html',  {'all_goods': all_goods})

class Backend18EditView(View):
    def post(self, request):
        print(request.POST.get('name'))
        print(request.POST.get('edit_name'))

        CreateDb18.objects.filter(category=request.POST.get('name')).update(category=request.POST.get('edit_name'))

        return redirect('/backendout18')