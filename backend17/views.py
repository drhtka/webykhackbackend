from django.views.generic.base import View
from backend17.models import CreateDb
from django.shortcuts import render, redirect

class Backend17View(View):
    # выводим товары
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category')
        return render(request, 'backend17/backend17.html', {'all_goods': all_goods})

class Backend17OutView(View):
    def post(self, request):

        len_null = ''
        print('123')
        print(request.POST.get('cat'))
        print(request.POST.get('mini'))
        print(request.POST.get('maxi'))
        price_start = 0
        price_end = 999999
        if request.POST.get('mini') != '':
            price_start = request.POST.get('mini')
            print(price_start)
        if request.POST.get('maxi') != '':
            price_end = request.POST.get('maxi')
            print(price_end)

        all_goods = CreateDb.objects.filter(category=request.POST.get('cat'))\
                                    .filter(price__gte=price_start)\
                                    .filter(price__lte=price_end)\
                                    .values_list('id', 'tovarname', 'price', 'sale', 'category')
        print('all_goods-26')
        print(all_goods)
        if len(all_goods) == 0:
            len_null = 'По таким критериям товаров нет'
        return render(request, 'backend17/backendout17.html', {'all_goods': all_goods, "len_null": len_null} )

class Backend17EditView(View):
    def post(self, request):
        print(request.POST.get('name'))
        print(request.POST.get('edit_name'))

        CreateDb.objects.filter(category=request.POST.get('name')).update(category=request.POST.get('edit_name'))

        return redirect('/backend17/')