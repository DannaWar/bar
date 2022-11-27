from django.db import models
from barApp.models import Producto, Trabajador
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField

# Create your models here.


User= get_user_model()

class Venta (models.Model):
    
    trabajador= models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha= models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Venta")
        verbose_name_plural =("Ventas")

    def __str__(self):
        return self.name
    
    @property
    def total(self):
        return self.Ventas_Producto_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
        )['total'] or FloatField(0)
    
   


class Ventas_Producto(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    id_venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad")
    fecha= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Ventas_Producto")
        verbose_name_plural =("Ventas_Productos")

    def __str__(self):
        return f'{self.cantidad} unidades de {self.id_producto.nombre_P}'
