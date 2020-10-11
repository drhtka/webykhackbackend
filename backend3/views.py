# -*- coding: utf-8 -*-

from django.views.generic.base import View

from django.shortcuts import render, redirect


class Backend3View(View):
    # выводим на страницу
    def get(self, request):

        return render(request, 'backend3/backend3.html')

class Backend3OutView(View):
    # записыаем в с список дел

    def get(self, request):


        #request.session['my_listt'] = []
        # if request.session['my_listt']: # если есть сессия вносим данные
        print(request.session.get('my_listt'))
        print('test')
        print(request.GET.get('text'))

        todo_task = request.GET.get('text')
        print(todo_task)
        request.session['my_listt'].append([todo_task])
        request.session.modified = True
        # else:
        #     request.session['my_listt'] = []

        return render(request, 'backend3/backend3.html', {'my_array': request.session['my_listt']})
