from django.views.generic.base import View
from backend24.models import CreateDb
from django.shortcuts import render, redirect

class Backend24View(View):
    # выводим товары
    def get(self, request):
        all_goods = CreateDb.objects.values_list('id', 'tovarname', 'price', 'sale', 'category', 'comments')
        return render(request, 'backend24/backend24.html', {'all_goods': all_goods})

class Backend24OutView(View):

    def post(self, request, pk):
        self.pk = pk
        # pk = request.POST.get('i')
        print(request.POST.get('comiments'))
        comments = request.POST.get('comiments')
        comments_id = CreateDb.objects.filter(id=pk).values_list('id', 'tovarname', 'price', 'sale', 'category', 'comments')
        comments_array = (comments_id[0][1], comments_id[0][2], comments_id[0][3], comments_id[0][4], comments)
        request.session['my_list'].append(comments_array)

        return render(request, 'backend24/backendout24.html', {'my_arr': request.session['my_list']})

class Backend24CompareView(View):

    def post(self, request):
        return render(request, 'backend24/backend24.html')