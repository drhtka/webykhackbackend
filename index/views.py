# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.template.response import TemplateResponse, HttpResponse
from django.views.generic.base import View


class IndexView(View):
    def get(self, request):
        #return HttpResponse('test')
        return render(request, 'index/index.html')