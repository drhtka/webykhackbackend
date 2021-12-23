from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from backend21.models import CreateDb
from django.shortcuts import render, redirect

class Backend21View(View):
    # выводим товары на странице товаров
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')
        return render(request, 'backend21/backend21.html', {'all_goods':all_goods })

class Backend21OutView(View):
    # Админка
    def post(self, request):
        request.session['my_list'] = ['ivan', '123456']
        auth_array = request.session['my_list']
        request.session['my_list'] = []
        sale_temp = []
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')
        if auth_array[0] == request.POST.get('login') and auth_array[1] == request.POST.get('email'):
            for all_goods_s in all_goods:

                sale_in_for = all_goods_s[0], all_goods_s[1], all_goods_s[2], int(all_goods_s[2]) - int(all_goods_s[2]) * 0.05, all_goods_s[4]
                sale_temp.append(sale_in_for)
            print('sale_temp')
            print(sale_temp)
            return render(request, 'backend21/backendout21.html', {'all_goods': sale_temp})
        return redirect('/backend21/')