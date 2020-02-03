"""gve URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from api import views
from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from rest_framework import routers

from api.views import CarroViewSet
from api.views import RegistroViewSet
from api.views import CdcViewSet


router = routers.DefaultRouter()
router.register(r'carros', CarroViewSet, basename='carros')
router.register(r'registros', RegistroViewSet, basename='registros')
router.register(r'cdcs', CdcViewSet, basename='cdcs')

urlpatterns = router.urls
