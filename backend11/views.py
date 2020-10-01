# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from backend11.models import CreatreUser
from django.shortcuts import render, redirect


class Backend11View(View):
    # выводим на страницу
    def get(self, request):
        return render(request, 'backend11/backend11.html')

class Backend11OutView(View):
    # удаляем и выводим на страницу
    def post(self, request):
        import hashlib
        site_users = request.POST.get('name')
        site_pass = request.POST.get('pass')
        hashed_password = hashlib.md5(request.POST.get('pass').encode())# кодируем
        final_ph = hashed_password.hexdigest()
        seve_site = CreatreUser(login_users=site_users, paass_users=final_ph)# заносим в базу
        seve_site.save()# заносим в базу
        return render(request, 'backend11/backendout11.html')

        #return render(request, 'backend13/backend10.html', {'all_goods': my_return})