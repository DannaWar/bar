from django import forms
from .models import Contacto

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #fields = ('nombre', 'email', 'tipo_consulta', 'mensaje')
        fields = '__all__'