# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
#from django.views import View
from django.shortcuts import render, redirect
# Create your views here.

class Backend1View(View):

    def get(self, request):

        return render(request, 'backend1/backend1.html',)

class Backend1OutView(View):

    def post(self, request):

        my_return = request.POST.get('fio'), request.POST.get('tel'), request.POST.get('mail')
        print(my_return)
        return render(request, 'backend1/backendout1.html', {'out_array': my_return})