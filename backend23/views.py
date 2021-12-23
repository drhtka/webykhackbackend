from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic.base import View
from backend22.models import CreateDb
from django.shortcuts import render, redirect

class Backend23View(View):
    # выводим товары на странице товаров
    def get(self, request):

        all_goods = CreateDb.objects.values_list()

        return render(request, 'backend23/backend23.html', {'all_goods':all_goods})

class Backend23OutView(View):
    # добавляе в карзину

    def get(self, request):
        print('11')
        print(request.session['my_listwtwo'])
        # if request.session.get('my_listwtwo'):

        # request.session['my_listwtwo'] = []
        id= request.GET.get('i')
        name = request.GET.get('name')
        price = request.GET.get('price')
        sale = request.GET.get('sale')
        categ = request.GET.get('categ')
        desc = request.GET.get('desc')
        my_array = [id, name, price, sale, categ, desc]
        list_temp = request.session['my_listwtwo']
        list_temp.append(my_array)

        request.session['my_listwtwo'] = list_temp
        print('listtwotwo')
        print(request.session['my_listwtwo'])
        return redirect(reverse('backend23'))


class Backend23CompareView(View):
    # сравнение
    def get(self, request):
        if request.session.get('my_listwtree'):
            print(request.session['my_listwtree'])
            return render(request, 'backend23/backendout23.html', {'my_arr': request.session['my_listwtree']})
        else:
            empty = 'Товары не выбраны'
            return render(request, 'backend23/backendout23.html', {'empty': empty})