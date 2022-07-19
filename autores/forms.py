from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model  = Autor
        fields = ['nome', 'pais', 'cidade', 'estado', 'telefone', 'email']