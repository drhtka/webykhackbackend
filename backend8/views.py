# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from backend11.models import CreatreUser
from django.shortcuts import render, redirect


class Backend8View(View):
    # выводим на страницу
    def get(self, request):
        my_array = [[0,'помыть посуду'], [1,'все-таки выучить html'], [2, 'Сделать домашку'], [3,'создать сайт']]
        request.session['my_list'] = my_array
        return render(request, 'backend8/backend8.html', {'my_array': my_array})

class BackendEdit8View(View):
    # выборка из сессии по id
    def post(self, request):
        todo_id = int(request.POST.get('id'))
        tmp_ses = request.session['my_list']
        print(tmp_ses[todo_id])
        return render(request, 'backend8/backendedit8.html', {'out_array': tmp_ses[todo_id]}) # срез по айди таски выводим в шаблон для редактирования

class Backend8OutView(View):
    # редактируем текст который в инпуте

    def post(self, request):
        id_task = int(request.POST.get('id'))
        edit_text = request.POST.get('edit')
        tmp_ses = request.session['my_list']
        tmp_ses[id_task][1] = edit_text
        request.session['my_list'] = tmp_ses
        return render(request, 'backend8/backend8.html', {'my_array': request.session['my_list']})
