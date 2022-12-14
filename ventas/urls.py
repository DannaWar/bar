from django.urls import path 
from .import views


app_name = "carro" 

urlpatterns = [
    path("registro_venta/", views.registro_venta, name="registro"),
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),    
    path("ventas/", views.ventas, name="ventas"),
]
