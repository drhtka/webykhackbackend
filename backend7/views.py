# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from backend11.models import CreatreUser
from django.shortcuts import render, redirect


class Backend7View(View):
    # выводим на страницу
    def get(self, request):
        my_array = [[0,'помыть посуду'], [1,'выиграть турнир'], [2,'Сделать домашку']]
        request.session['my_list'] = my_array
        return render(request, 'backend7/backend7.html', {'my_array': my_array})

class BackendDel7View(View):
    # удаляем из сессии
    def post(self, request):
        id_del = int(request.POST.get('id'))
        my_test_ses = request.session['my_list']
        #my_counter = 0
        for my_test_ses_s in my_test_ses:
            if my_test_ses_s[0] == id_del:
                print('test')
                print(my_test_ses_s[0])
                del my_test_ses[0]
            #my_counter += 1
        request.session['my_list'] = my_test_ses
        return render(request, 'backend7/backend7.html', {'my_array': request.session['my_list']})

