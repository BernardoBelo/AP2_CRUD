from django.db import models

# Create your models here.

class Motos(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    data_de_nascimento = models.CharField(max_length=30)
    endereco = models.CharField(max_length=200)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    ano = models.IntegerField()
    contato = models.CharField(max_length=30)
    
