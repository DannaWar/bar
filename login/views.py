from django.shortcuts import render
from .forms import UserRegisterForm
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

