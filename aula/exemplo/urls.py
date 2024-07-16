from django.contrib.auth import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('teste',views.teste),
    path('saudacao',views.saudacao),
    path('parametro/<str:nome>',views.parametro),
    path('contar/<str:nome>',views.contar),
    path('index',views.index),
    path('person<int:id>',views.person),
]