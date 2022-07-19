from django.db import models

class Compra(models.Model):
    FORMA = (
        ('cartão_de_débito', 'Cartão de Débito'),
        ('cartão_de_crédito', 'Cartão de Crédito'),
        ('boleto', 'Boleto'),
        ('pix', 'Pix'),
    )

    codigo              = models.BigAutoField(primary_key=True)
    efetuada_em         = models.DateTimeField(auto_now_add=True)

    nome_do_cliente      = models.CharField(max_length=100)
    sobrenome_do_cliente = models.CharField(max_length=100)
    usuario              = models.CharField(max_length=50)
    email                = models.EmailField(blank=True)
    endereco             = models.CharField(max_length=100)
    segundo_endereco     = models.CharField(max_length=100, blank=True)
    # pais                 = models.CharField(
    #     max_length=100
    # )
    # estado               = models.CharField(
    #     max_length=30
    # )
    CEP                  = models.BigIntegerField()
    forma_pagamento      = models.CharField(
        max_length=17,
        choices=FORMA,
    )
    nome_no_cartao       = models.CharField(max_length=100)
    numero_do_cartao     = models.BigIntegerField()
    validade_do_cartao   = models.CharField(max_length=5)
    cvv                  = models.IntegerField()
        
    def __str__(self):
        return self.codigo
