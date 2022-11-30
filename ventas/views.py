from django.shortcuts import render
from .carro import Carro
from ventas.models import Producto
from django.shortcuts import redirect
from pedidos.models import LineaPedido




# Create your views here.
def registro_venta(request):   
     
     producto=Producto.objects.all()
    
     return render(request, "registro_venta.html", {"productos":producto})    
    
def agregar_producto(request, producto_id):
     carro=Carro(request)
     
     producto=Producto.objects.get(id=producto_id)
     
     carro.agregar(producto=producto)
     pass
     return redirect('producto')
 
 
def eliminar_producto(request, producto_id):
     carro=Carro(request)
     
     producto=Producto.objects.get(id=producto_id)
     
     carro.eliminar(producto=producto)
     
     return redirect('carro:registro')
 
 

def restar_producto(request, producto_id):
     carro=Carro(request)
     
     producto=Producto.objects.get(id=producto_id)
     
     carro.restar_producto(producto=producto)
     
     return redirect('carro:registro')
 

def limpiar_carro(request, producto_id):
     carro=Carro(request)
     
     carro.limpiar_carro()
     
     return redirect('carro:registro')

def ventas(request):
     venta= LineaPedido.objects.all()
     
     return render(request, 'ventas.html', {'ventas':venta})
