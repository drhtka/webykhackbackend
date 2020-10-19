# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.base import View

from django.shortcuts import render, redirect


class Backend2View(View):
    # выводим на страницу

    def get(self, request):
        request.session['my_list_six'] = []
        # arPass = [
        #             {'numb':6574543},
        #             {'numb':8790431},
        #             {'numb':7273654},
        #           ]

        arPass = [
                    '6574543',
                    '8790431',
                    '7273654',
                  ]

        request.session['my_list_six'] = arPass

        return render(request, 'backend2/backend2.html', {'my_array': arPass})

class Backend2OutView(View):
    #  создаем массив

    def post(self, request):
        input_key = request.POST.get('text')
        print('input_key')
        print(input_key)
        my_test_ses = request.session['my_list_six']
        print('my_test_ses')
        print(my_test_ses)

        if input_key != '':
            my_return = ''

            real_pass = 'Правильный Динамический пароль для вас 7273654'
            for arPass_s in my_test_ses:
                print('arPass_s')
                print(arPass_s)
                if arPass_s == input_key:
                    print('ura')
                    #my_return = my_test_ses
                    print('my_return')
                    print(my_return)
                    #break
                    return render(request, 'backend2/backendout2.html')
                    #break
            if my_return == '': # общая проверка
                print('else')
                return render(request, 'backend2/backerr2.html', {'real_pass': real_pass})
                    #
                    #return HttpResponse('Не верный ключ активации <a href="http://127.0.0.1:8888/backend2/">Вернуться назад</a>')
        #return render(request, 'backend2/backend2.html')

    # def get(self, request):
    #     return
