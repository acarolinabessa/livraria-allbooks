from django.db import models

class Compra(models.Model):
    FORMA = (
        ('cartão_de_débito', 'Cartão de Débito'),
        ('cartão_de_crédito', 'Cartão de Crédito'),
        ('boleto', 'Boleto'),
        ('pix', 'Pix'),
    )

    ESTADOS = (
        ('acre', 'Acre'),
        ('alagoas', 'Alagoas'),
        ('amapa', 'Amapá'),
        ('amazonas', 'Amazonas'),
        ('bahia', 'Bahia'),
        ('ceara', 'Ceará'),
        ('distrito_federal', 'Distrito Federal'),
        ('espirito_santos', 'Espírito Santo'),
        ('goais', 'Goiás'),
        ('maranhao', 'Maranhão'),
        ('mato_grosso', 'Mato Grosso'),
        ('mato_grosso_do_sul', 'Mato Grosso do Sul'),
        ('minas_gerais', 'Minas Gerais'),
        ('para', 'Pará'),
        ('paraiba', 'Paraíba'),
        ('parana', 'Paraná'),
        ('pernambuco', 'Pernambuco'),
        ('piaui', 'Piauí'),
        ('rio_de_janeiro', 'Rio de Janeiro'),
        ('rio_grande_do_norte', 'Rio Grande do Norte'),
        ('rio_grande_do_sul', 'Rio Grande do Sul'),
        ('rondonia', 'Rondônia'),
        ('roraima', 'Roraima'),
        ('santa_catarina', 'Santa Catarina'),
        ('sao_paulo', 'São Paulo'),
        ('sergipe', 'Sergipe'),
        ('tocantins', 'Tocantins'),
    )

    PAISES = (
        ('brasil', 'Brasil'),
    )

    codigo              = models.BigAutoField(primary_key=True)
    efetuada_em         = models.DateTimeField(auto_now_add=True)

    nome_do_cliente      = models.CharField(max_length=100)
    sobrenome_do_cliente = models.CharField(max_length=100)
    usuario              = models.CharField(max_length=50)
    email                = models.EmailField(blank=True)
    endereco             = models.CharField(max_length=100)
    segundo_endereco     = models.CharField(max_length=100, blank=True)
    pais                 = models.CharField(
        max_length=100,
        choices=PAISES,
        default="Escolha..."
    )
    estado               = models.CharField(
        max_length=100,
        choices=ESTADOS,
        default="Escolha..."
    )
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
