from django.shortcuts import render
from .forms import UserRegisterForm, productoForm
from django.contrib import messages


# Create your views here.

def register(request):
    
    form=UserRegisterForm()
    
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario= form.cleaned_data["username"]
            messages.success(request, f'Usuario {usuario} creado')  
    else:
            form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})

def usuario(request):
    
    return render(request, 'usuario.html')


def crear_producto(request):
    form=productoForm()
    if request.method == 'POST':
        form=productoForm(request.POST)
        if form.is_valid():
            form.save()
            producto= form.cleaned_data["nombre_P"]
            messages.success(request, f'Producto{producto} creado')  
    else:
            form = productoForm()
    return render(request, 'crear_producto.html',{"form": form})
