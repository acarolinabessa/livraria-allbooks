from django.db import models

class Editora(models.Model):
    nome     = models.CharField(max_length=100)
    CNPJ     = models.BigIntegerField()
    endereco = models.CharField(max_length=80)
    cidade   = models.CharField(max_length=45)
    estado   = models.CharField(max_length=45)
    telefone = models.BigIntegerField()
    email    = models.EmailField()
    
    def __str__(self):
        return self.nome
