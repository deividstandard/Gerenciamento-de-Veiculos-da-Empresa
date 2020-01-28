from django.db import models

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Carro(models.Model):
    '''
    Definição de atributos para recurso
    carro
    '''

    class Meta:
        db_table = 'carro'

    id_carro = models.AutoField(primary_key=True)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    placa = models.CharField(max_length=10, unique=True)
    quilometragem = models.IntegerField()

    def __str__(self):
        return self.placa + ' - ' + self.modelo.upper()


class Cdc(models.Model):
    '''
    Definição de atributos para recurso
    carro
    '''

    class Meta:
        db_table = 'cdc'

    id_cdc = models.AutoField(primary_key=True)
    data_criacao = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome.upper()


class Registro(models.Model):
    '''
    Definição de atributos para recurso
    registro
    '''

    class Meta:
        db_table = 'registro'

    id_registro = models.AutoField(primary_key=True)
    data_inicial = models.DateField(auto_now_add=True)
    data_final = models.DateField()
    condutor = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=200, blank=False)
    quilometragem_inicial = models.IntegerField()
    quilometragem_final = models.IntegerField()
    id_carro = models.OneToOneField(
        Carro, on_delete=models.SET_NULL, null=True)
    id_cdc = models.OneToOneField(Cdc, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.condutor + ' - ' + self.descricao
