# -*- coding: utf-8 -*-
"""webykhackbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from index.views import IndexView

from backend1.views import Backend1View, Backend1OutView
from backend2.views import Backend2View, Backend2OutView
from backend3.views import Backend3View, Backend3OutView
from backend4.views import Backend4View, Backend4OutView
from backend5.views import Backend5View, Backend5OutView
from backend6.views import Backend6View, Backend6OutView
from backend7.views import Backend7View, BackendDel7View
from backend8.views import Backend8View, Backend8OutView, BackendEdit8View
from backend9.views import Backend9View, Backend9OutView
from backend10.views import Backend10View, Backend10OutView
from backend11.views import Backend11View, Backend11OutView
from backend12.views import Backend12View, Backend12OutView
from backend13.views import Backend13View, Backend13OutView, BackCreateProd13
from backend14.views import Backend14View, Backend14OutView
from backend15.views import Backend15View, Backend15OutView
from backend16.views import Backend16View, Backend16OutView
from backend17.views import Backend17View, Backend17OutView, Backend17EditView
from backend18.views import Backend18View, Backend18OutView, Backend18EditView
from backend19.views import Backend19View, Backend19OutView
from backend20.views import Backend20View, Backend20OutView, Backend20DelView
from backend21.views import Backend21View, Backend21OutView
from backend22.views import Backend22View, Backend22OutView, Backend22CompareView
from backend24.views import Backend24View, Backend24OutView, Backend24CompareView
from backend25.views import Backend25View, Backend25OutView, Backend25CompareView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('backend1/', Backend1View.as_view(), name='backend1'),
    path('backendout1'
         '', Backend1OutView.as_view(), name='backendout1'),

    path('backend2/', Backend2View.as_view(), name='backend2'),
    path('backendout2', Backend2OutView.as_view(), name='backendout2'),

    path('backend3/', Backend3View.as_view(), name='backend3'),
    path('backendout3', Backend3OutView.as_view(), name='backendout3'),

    path('backend4/', Backend4View.as_view(), name='backend4'),
    path('backendout4', Backend4OutView.as_view(), name='backendout4'),

    path('backend5/', Backend5View.as_view(), name='backend5'),
    path('backendout5/', Backend5OutView.as_view(), name='backendout5'),

    path('backend6/', Backend6View.as_view(), name='backend6'),
    path('backendout6', Backend6OutView.as_view(), name='backendout6'),

    path('backend7/', Backend7View.as_view(), name='backend7'),
    path('backenddel7', BackendDel7View.as_view(), name='backenddel7'),

    path('backend8/', Backend8View.as_view(), name='backend8'),
    path('backendedit8', BackendEdit8View.as_view(), name='backendedit8'),
    path('backendout8', Backend8OutView.as_view(), name='backendout8'),

    path('backend9/', Backend9View.as_view(), name='backend9'),
    path('backendout9', Backend9OutView.as_view(), name='backendout9'),

    path('backend10/', Backend10View.as_view(), name='backend10'),
    path('backendout10', Backend10OutView.as_view(), name='backendout10'),

    path('backend11/', Backend11View.as_view(), name='backend11'),
    path('backendout11', Backend11OutView.as_view(), name='backendout11'),

    path('backend12/', Backend12View.as_view(), name='backend12'),
    path('backendout12', Backend12OutView.as_view(), name='backendout12'),

    path('backend13/', Backend13View.as_view(), name='backend13'),
    path('backendout13/', Backend13OutView.as_view(), name='backendout13'),
    path('backcreate13/', BackCreateProd13.as_view(), name='backcreate13'),

    path('backend14/', Backend14View.as_view(), name='backend14'),
    path('backendout14/', Backend14OutView.as_view(), name='backendout14'),

    path('backend15/', Backend15View.as_view(), name='backend15'),
    path('backendout15', Backend15OutView.as_view(), name='backendout15'),

    path('backend16/', Backend16View.as_view(), name='backend16'),
    path('backendout16', Backend16OutView.as_view(), name='backendout16'),

    path('backend17/', Backend17View.as_view(), name='backend17'),
    path('backendout17', Backend17OutView.as_view(), name='backendout17'),
    path('backendedit17', Backend17EditView.as_view(), name='backendedit17'),

    path('backend18/', Backend18View.as_view(), name='backend18'),
    path('backendout18', Backend18OutView.as_view(), name='backendout18'),
    path('backendedit18', Backend18EditView.as_view(), name='backendedit18'),

    path('backend19/', Backend19View.as_view(), name='backend19'),
    path('backendout19', Backend19OutView.as_view(), name='backendout19'),

    path('backend20/', Backend20View.as_view(), name='backend20'),
    path('backendout20', Backend20OutView.as_view(), name='backendout20'),
    path('backenddel20', Backend20DelView.as_view(), name='backenddel20'),

    path('backend21/', Backend21View.as_view(), name='backend21'),
    path('backendout21', Backend21OutView.as_view(), name='backendout21'),

    path('backend21/', Backend21View.as_view(), name='backend21'),
    path('backendout21', Backend21OutView.as_view(), name='backendout21'),

    path('backend22/', Backend22View.as_view(), name='backend22'),
    path('backendout22', Backend22OutView.as_view(), name='backendout22'),
    path('backendcompare22', Backend22CompareView.as_view(), name='backendcompare22'),

    path('backend24/', Backend24View.as_view(), name='backend24'),
    path('backendout24/<int:pk>/', Backend24OutView.as_view(), name='backendout24'),
    path('backendcompare24', Backend24CompareView.as_view(), name='backendcompare24'),

    path('backend25/', Backend25View.as_view(), name='backend25'),
    path('backendout25/', Backend25OutView.as_view(), name='backendout25'),
    path('backendcompare25', Backend25CompareView.as_view(), name='backendcompare25'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
