from django.shortcuts import render
from .models import Producto
from .forms import ContactForm

# Create your views here.
def index(request):
    return render(request,'inicio.html')

def eventos(request):
    return render(request,'eventos.html')

def hot(request):
    
    productos= Producto.objects.filter(categoria_P="hot")
    
    return render(request,'hot.html', {"productos": productos})

def cold(request):
    
    productos= Producto.objects.filter(categoria_P="cold")
    
    return render(request,'cold.html', {"productos": productos})

def food(request):
    
    productos=Producto.objects.filter(categoria_P="food")
    
    return render(request,'food.html', {"productos": productos})

def producto(request):
    
    product_cold=Producto.objects.filter(categoria_P="cold") [:3]
    product_hot=Producto.objects.filter(categoria_P="hot")[:3]
    product_food=Producto.objects.filter(categoria_P="food") [:3]
    
    
    return render(request,'producto.html', {"product_cold": product_cold, "product_food": product_food, "product_hot": product_hot})
    

def nosotros(request):
    
    return render(request, 'nosotros.html')


def contacto (request):
    data = {
        'form': ContactForm()
    }
    
    if request.method == 'POST':
        formulario = ContactForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto enviado!"
            
        else:
            data["form"] = formulario
            
    return render(request, 'contacto.html', data)

def cafe (request):
    return render(request, 'cafe.html')


def galeria(request):
    
    return render(request, 'galeria.html')