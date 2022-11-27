from django.contrib import admin
from .models import Factura,Factura_Producto,Producto,Producto_Proveedor,Proveedor,Trabajador, Contacto


# Register your models here.

admin.site.register(Factura)
admin.site.register(Factura_Producto)
admin.site.register(Producto)
admin.site.register(Producto_Proveedor)
admin.site.register(Proveedor)
admin.site.register(Trabajador)
admin.site.register(Contacto)