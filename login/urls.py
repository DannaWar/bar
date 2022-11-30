from django.urls import path 
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
   
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", LogoutView.as_view(template_name="inicio.html"), name="logout"),
    path("usuario/",views.usuario, name="usuario"),
    path("crear_producto", views.crear_producto, name="crear_producto"),
] 