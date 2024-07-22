from django.contrib.auth import admin
from django.urls import path, include
from exemplo import views

app_name = 'exemplo'

urlpatterns = [
    path('teste',views.teste),
    path('saudacao',views.saudacao),
    path('parametro/<str:nome>',views.parametro),
    path('contar/<str:nome>',views.contar),
    path('index',views.index),
    path('person/read/<int:id>',views.read, name="read_pessoa"),
    path('persons', views.list_persons, name="pessoas"),
    path('person/delete/<int:id>',views.delete, name="delete_pessoa"),
]