from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from backend20.models import CreateDb
from django.shortcuts import render, redirect

class Backend20View(View):
    # выводим товары на странице товаров
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')

        return render(request, 'backend20/backend20.html', {'all_goods':all_goods})

class Backend20OutView(View):
    # добавляе в карзину
    def get(self, request):

        # request.session.get('my_listto')
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')
        id= request.GET.get('i')
        name = request.GET.get('name')
        price= request.GET.get('price')
        sale = request.GET.get('sale')
        categ = request.GET.get('categ')
        my_array = [id, name, price, sale, categ]
        # for my_array in my_array:
        # # request.session['my_listto'] = []
        # if my_array[0] == all_goods[0][0]:
        #     print("1 id")
        #     print(my_array[0], all_goods[0][0])
        #     return render(request, 'backend20/backend20.html', {'all_goods':all_goods, 'my_arr': request.session['my_listto']})
        # # break
        # else:
        #     print('my_array')
        #     print(request.session['my_listto'])
        request.session['my_listto'].append(my_array)
        request.session.modified = True
        return redirect('/backenddel20')
        # print('my_array')
        # print(request.session['my_listto'])
        # return render(request, 'backend20/backend20.html', {'all_goods':all_goods, 'my_arr': request.session['my_listto']})

class Backend20DelView(View):
    # удаление
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')

        id_del = request.GET.get('i') # ловим по id
        id_del = id_del
        i = 0
        my_test_ses = request.session['my_listto'] # сессию в переменную
        for my_test_ses_s in my_test_ses: # перебераем фором чтоб не падало
            if my_test_ses_s[0] == id_del:
                del my_test_ses[i] # удаляем все по 0 айдишнику
                break
            i += 1
            request.session['my_listto'] = my_test_ses
            request.session.modified = True
        return render(request, 'backend20/backend20.html', {'all_goods':all_goods, 'my_arr': request.session['my_listto']})