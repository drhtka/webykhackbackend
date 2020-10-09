# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from backend11.models import CreatreUser
from django.shortcuts import render, redirect


class Backend5View(View):
    # выводим на страницу
    def get(self, request):
        request.session['my_list'] = []
        my_array = [[1, 'iphone 7', 300, 0],
                    [2, 'iphone 8', 400, 1],
                    [3, 'iphone X', 600, 0],
                    [4, 'iphone 7plus', 600, 1],
                    [5, 'iphone 6 plus', 600, 0],
                    ]
        request.session['my_list'] = my_array
        return render(request, 'backend5/backend5.html', {'my_array': my_array})

class Backend5OutView(View):
    # удаляем из сессии
    def get(self, request):
        product_id = request.GET.get('i')
        print(product_id)
        out_array = ''
        for item in request.session['my_list']:
            print('t')
            print(item[0])
            if str(item[0]) == product_id:
                out_array = item
                out_array[3] += 1
                break
        print(out_array)

        return render(request, 'backend5/backendout5.html', {'out_array': out_array})

