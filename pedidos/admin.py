
from django.contrib import admin
from .models import Pedido, LineaPedido

# Register your models here.
admin.site.register([Pedido, ])

class lista_ventas(admin.ModelAdmin):
    list_display= ("user", "producto", "pedido", "cantidad", "created_at", "importe")
    search_fields = ('producto',)
    ordering = ('created_at',)
    list_filter = ('created_at','pedido',)

admin.site.register(LineaPedido, lista_ventas)

# Register your models here