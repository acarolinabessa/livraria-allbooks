from django.db import models

class Autor(models.Model):
    nome     = models.CharField(max_length=100)
    pais     = models.CharField(max_length=45)
    cidade   = models.CharField(max_length=45)
    estado   = models.CharField(max_length=45)
    telefone = models.BigIntegerField(blank=True)
    email    = models.EmailField(blank=True)
    
    def __str__(self):
        return self.nome
