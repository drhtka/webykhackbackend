# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from backend11.models import CreatreUser
from django.shortcuts import render, redirect


class Backend10View(View):
    # выводим на страницу
    def get(self, request):
        my_array = [[0,'kivy', 25], [1,'apple', 30], [2, 'banana', 25]]
        request.session['my_list'] = my_array
        y_sum = 0
        for my_array_s in my_array:
            y_sum =  y_sum + my_array_s[2]
        return render(request, 'backend10/backend10.html', {'beckend10': request.session['my_list'], 'y_sum': y_sum})

class Backend10OutView(View):
    # удаляем и выводим на страницу
    def post(self, request):

        return render(request, 'backend10/backendout10.html')