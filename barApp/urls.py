from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("eventos/", views.eventos, name="eventos"),
    path("hot/", views.hot, name="hot"),
    path("cold/", views.cold, name="cold"),
    path("food/", views.food, name="food"),
    path("producto/", views.producto, name="producto"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("contacto/", views.contacto, name="contacto"),
] 