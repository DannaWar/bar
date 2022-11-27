from django.contrib import admin
from .models import Venta, Ventas_Producto

# Register your models here.
admin.site.register([Venta, Ventas_Producto ])