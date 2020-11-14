# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from backend11.models import CreatreUser
from django.shortcuts import render, redirect
import operator

class Backend4View(View):
    # выводим на страницу
    def get(self, request):

        request.session['my_list'] = []
        tmp_my_array = [{'id': 1, 'name': 'iphone7 ', 'price': 700, 'view': 5},
                    {'id': 3, 'name': 'iphone6 ', 'price': 400, 'view': 1},
                    {'id': 2, 'name': 'iphoneX ', 'price': 600, 'view': 3}]

        request.session['my_list'] = [tmp_my_array]
        #print(request.session['my_list'][0])
        return render(request, 'backend4/backend4.html', {'my_array': request.session['my_list'][0]})

class Backend4OutView(View):
    # удаляем из сессии

    def get(self, request):
        my_sort = request.session['my_list'][0]
        #print(my_sort)
        final_array = []
        for i in sorted(my_sort, key=operator.itemgetter('price')):
            final_array.append(i)
        print(final_array)
        return render(request, 'backend4/backend4.html', {'my_array': final_array})
