from django.contrib import admin
from django.contrib import messages
from .models import Factura,Factura_Producto,Producto,Producto_Proveedor,Proveedor,Trabajador, Contacto



# Register your models here.

    
admin.site.register(Factura)
admin.site.register(Factura_Producto)

class Productoadmin(admin.ModelAdmin):
    list_display = ('nombre_P', 'categoria_P', 'descripcion_P', 'precio_P',)
    search_fields = ('nombre_P', 'descripcion_P')
    ordering = ('-nombre_P',)
   
    
    def rate_five_stars(modeladmin, request, queryset):
        queryset.update(rating=5.0)
        messages.success(request, "Se calificó con 5 estrellas")

    admin.site.add_action(rate_five_stars, "Calificar con 5 estrellas")
admin.site.register(Producto, Productoadmin)


admin.site.register(Producto_Proveedor)
admin.site.register(Proveedor)

class Trabajadoradmin(admin.ModelAdmin):
    list_display = ('nom_T', 'apellido_T', 'direccion_T',)
    search_fields = ('nom_T', 'apellido_T')
    ordering = ('-nom_T',)
admin.site.register(Trabajador, Trabajadoradmin)

class Contactoadmin(admin.ModelAdmin):
    list_display = ('nombre','email', 'tipo_consulta', 'mensaje',)
    search_fields = ('nombre', 'tipo_consulta')
    ordering = ('-nombre',)
admin.site.register(Contacto, Contactoadmin)

admin.site.site_header = ' Café/Bar Oh la lá'
admin.site.index_title = 'Panel de control de mi sitio'
admin.site.site_title = 'Oh la lá'


