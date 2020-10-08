# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from backend11.models import CreatreUser
from django.shortcuts import render, redirect


class Backend6View(View):
    # выводим на страницу
    def get(self, request):
        request.session['my_list'] = []
        my_array = [[0, 'iphone 7', 300, 0],
                    [1, 'iphone 8', 400, 1],
                    [2, 'iphone X', 600, 0],
                    [3, 'iphone 7plus', 600, 1],
                    [4, 'iphone 6 plus', 600, 0],
                    ]
        request.session['my_list'] = my_array
        return render(request, 'backend6/backend6.html', {'my_array': my_array})

class Backend6OutView(View):
    # удаляем из сессии
    def post(self, request):
        search_name = request.POST.get('name_phone')
        my_test_ses = request.session['my_list']
        #my_counter = 0
        my_return = ''
        if search_name != '':
            for my_test_ses_s in my_test_ses:
                if my_test_ses_s[1] == search_name:
                    print(my_test_ses_s[1])
                    my_return = my_test_ses_s
                    print(my_return)
                    request.session['my_list'] = my_return

                    return render(request, 'backend6/backendout6.html', {'out_array': request.session['my_list']})
                else:
                    return HttpResponse("<p>Товара с таким именем - не найдено!</p>")

