# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
#from django.views import View
from django.shortcuts import render, redirect
# Create your views here.

class Backend1View(View):

    def get(self, request):
        #request.session['my_list'] = []
        my_array = [[1, 'iphone 7', 300, 0],
                    [2, 'iphone 8', 400, 1],
                    [3, 'iphone X', 600, 0],
                    [2, 'iphone 7plus', 600, 1],
                    [3, 'iphone 6 plus', 600, 0],
                    ]
        request.session['my_list'] = my_array
        return render(request, 'backend1/backend1.html', {'out_array': request.session['my_list']})

class Backend1OutView(View):

    def post(self, request):
        print(request.session['my_list'])
        todo_id = request.POST.get('name_phone')
        print(todo_id)
        if request.POST.get('name_phone') != '':
            my_return = ''
            for item in request.session['my_list']:
                #print(item)
                if item[1] == todo_id:
                    my_return = item
                    print('my_return')
                    print(request.session['my_list'])
        else:
            return redirect('backend1')

        return render(request, 'backend1/backendout1.html', {'out_array': my_return})