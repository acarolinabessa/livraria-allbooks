from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model  = Livro
        fields = [
            'titulo', 'categoria', 'autor', 
            'editora', 'IBSN', 'edicao', 
            'data_de_impressao', 'traducao', 'numero_de_paginas', 
            'quantidade_em_estoque', 'descricao', 'valor', 
            'desconto', 'imagem'
        ]