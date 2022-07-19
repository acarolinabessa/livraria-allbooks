from django.db import models
from editoras.models import Editora
from autores.models import Autor

class Livro(models.Model):
    titulo                = models.CharField(max_length=50)
    categoria             = models.CharField(max_length=50)
    autor                 = models.ManyToManyField(Autor)
    editora               = models.ManyToManyField(Editora)
    IBSN                  = models.BigIntegerField()
    edicao                = models.IntegerField()
    data_de_impressao     = models.DateField()
    traducao              = models.CharField(max_length=100, blank=True)
    numero_de_paginas     = models.IntegerField()
    quantidade_em_estoque = models.IntegerField()
    descricao             = models.TextField()
    valor                 = models.DecimalField(max_digits=9, decimal_places=2)
    desconto              = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    imagem                = models.ImageField(upload_to="uploads", blank=True)

    def __str__(self):
        return self.titulo