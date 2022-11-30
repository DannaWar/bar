from datetime import datetime
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Trabajador (models.Model):
    nom_T = models.CharField("Nombre",max_length=45)
    apellido_T = models.CharField("Apellido",max_length=45)
    direccion_T = models.CharField("Dirección",max_length=45)
    telefono_T = models.CharField("Teléfono", max_length=45)
    email= models.CharField("Correo electrónico", max_length=45)
    
    class Meta:
        verbose_name_plural = "Trabajadores"
        
    def __str__(self):
        return "%s %s" %(self.nom_T, self.apellido_T)
    
class Factura (models.Model):
    fecha_F = models.DateField("Fecha factura",auto_now=False, auto_now_add=False)    
    id_T = models.ForeignKey(Trabajador, on_delete=models.CASCADE, verbose_name="Trabajadores")
    
    class Meta:
        verbose_name_plural = "Facturas"
    
    def __str2__(self):
        
        return "%s" (self.fecha_F)
    
class Producto (models.Model):
    
    CATEGORIA_PRODUCTOS=[
        ("hot", "Bebidas calientes"),
        ("cold", "Bebidas frías"),
        ("food", "Alimentos"),
    ]
    nombre_P = models.CharField( "Nombre del producto",max_length=45)
    categoria_P= models.CharField( "Categoria del producto", max_length=45 , choices=CATEGORIA_PRODUCTOS)
    descripcion_P = models.CharField( "Descripción del producto",max_length=200)
    cantidad_P = models.IntegerField("Cantidad del producto",)
    precio_P = models.IntegerField("Precio del producto",)
    imagen_P = models.ImageField("Imagen del producto", upload_to="static/imagenes/DB")
    
    def __str__(self):
        return "Nombre: %s Cantidad: %s Precio: %s" % (self.nombre_P, self.cantidad_P, self.precio_P)
    
class Factura_Producto(models.Model):
    cod_F = models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name="Código Factura")
    cod_P = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Código Producto")
    
class Proveedor(models.Model):
    nom_Pr = models.CharField("Nombre del proveedor", max_length=45)
    direccion_Pr = models.CharField("Dirección del proveedor", max_length=45)
    telefono_Pr = models.CharField( "Teléfono del proveedor",max_length=45)
    correo_Pr = models.EmailField("Correo electrónico", max_length=254)
    
    class Meta:
        verbose_name_plural= "Proveedores"
        
    def __str__(self):
        return "Proveedor: %s" % self.nom_Pr 
    
class Producto_Proveedor(models.Model):
    cod_P = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Código Producto")
    id_Pr = models.ForeignKey(Proveedor, on_delete=models.CASCADE, verbose_name="Código Proveedor")
    
    class Meta:
        verbose_name_plural="Producto_Proveedores"
        

opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]

        
class Contacto (models.Model):
    nombre= models.CharField(max_length=45)
    email= models.EmailField()
    tipo_consulta= models.IntegerField(choices=opciones_consultas)
    mensaje= models.TextField()
    
    def __str__(self):
        return self.nombre
            


