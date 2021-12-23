from django.views.generic.base import View
from backend25.models import CreateDb
from django.shortcuts import render, redirect

class Backend25View(View):
    # выводим товары
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category', 'comment_one', 'comment_two',)
        print('all_goods-0')
        print(all_goods)
        return render(request, 'backend25/backend25.html', {'all_goods': all_goods})

class Backend25OutView(View):

    def post(self, request):

        id_com = request.POST.get('i')
        comment_o = request.POST.get('comments_o')
        comments_t = request.POST.get('comments_t')
        # prod_id = CreateDb.objects.values('id')
        # prod_id = prod_id[0]['id']

        print('prod_id')
        print(id_com)
        print(comment_o)
        print(comments_t)
        # if prod_id == id_com:
        CreateDb.objects.filter(id=id_com).update(comment_one=comment_o, comment_two=comments_t)
        all_goods = CreateDb.objects.values_list()
# доделать вывод на главную
        print('all_goods-1')
        print(all_goods[0])
        return render(request, 'backend25/backendout25.html', {'all_goods': all_goods})

class Backend25CompareView(View):

    def post(self, request):
        return render(request, 'backend25/backend25.html')