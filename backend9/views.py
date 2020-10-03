# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from backend11.models import CreatreUser
from django.shortcuts import render, redirect


class Backend9View(View):
    # выводим на страницу
    def get(self, request):
        my_array = [[0, 'iphone7'], [1, 'iphone8'], [2, 'iphone9']]
        request.session['my_list'] = my_array
        return render(request, 'backend9/backend9.html', {'beckend9': request.session['my_list']})

class Backend9OutView(View):
    # удаляем и выводим на страницу
    def post(self, request):
        print('111111')
        heart = request.POST.get('datacard')
        out_array = heart[1: -1]

        count_out_array = len(out_array.split(','))
        return render(request, 'backend9/backendout9.html', {'out_array': out_array, 'count_out_array': count_out_array})
