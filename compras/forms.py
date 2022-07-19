from django import forms
from crispy_forms.helper import FormHelper
from .models import Compra

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ['nome_do_cliente', 'sobrenome_do_cliente', 'usuario', 'email', 'endereco', 'segundo_endereco', 'CEP', 'estado', 'pais', 'nome_no_cartao', 'numero_do_cartao', 'validade_do_cartao', 'cvv']
        widgets = {
            'nome_do_cliente': forms.TextInput(attrs={'placeholder': 'Primeiro nome'}),
            'sobrenome_do_cliente': forms.TextInput(attrs={'placeholder': 'Último nome'}),
            'usuario': forms.TextInput(attrs={'placeholder': 'Usuário'}),
            'email': forms.TextInput(attrs={'placeholder': 'fulano@exemplo.com'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Rua dos bobos, n° 0'}),
            'segundo_endereco': forms.TextInput(attrs={'placeholder': 'Apartamento ou casa'}),
        }

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 

