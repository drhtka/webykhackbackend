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
from django.contrib import admin
from django.urls import path
from index.views import IndexView

from backend1.views import Backend1View, Backend1OutView
from backend9.views import Backend9View, Backend9OutView
from backend10.views import Backend10View, Backend10OutView
from backend11.views import Backend11View, Backend11OutView
from backend12.views import Backend12View, Backend12OutView
from backend13.views import Backend13View, Backend13OutView
from backend14.views import Backend14View, Backend14OutView
from backend15.views import Backend15View, Backend15OutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('backend1/', Backend1View.as_view(), name='backend1'),
    path('backendout1/', Backend1OutView.as_view(), name='backendout1'),
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
    path('backend14/', Backend14View.as_view(), name='backend14'),
    path('backendout14/', Backend14OutView.as_view(), name='backendout14'),
    path('backend15/', Backend15View.as_view(), name='backend15'),
    path('backendout15', Backend15OutView.as_view(), name='backendout15'),
]
