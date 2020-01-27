from django.db import models

# Create your models here.


class Carro(models.Model):
    '''
    Definição de atributos para recurso
    carro
    '''

    class Meta:

        db_table = 'carro'

    id_carro = models.IntegerField(primary_key=True, unique=True)
    data_criacao = models.DateField(auto_now_add=True)
    placa = models.CharField(max_length=10)
    quilometragem = models.IntegerField()

    def __str__(self):
        return self.id_carro


class Registro(models.Model):
    '''
    Definição de atributos para recurso
    registro
    '''

    class Meta:

        db_table = 'registro'

    id_registro = models.IntegerField(primary_key=True, unique=True)
    data_inicial = models.DateField(auto_now_add=True)
    data_final = models.DateField()
    condutor = models.CharField(max_length=50, blank=False, null=False)
    descricao = models.CharField(max_length=200, blank=False)
    quilometragem_inicial = models.IntegerField()
    quilometragem_final = models.IntegerField()
    id_carro = models.OneToOneField(
        Carro,
        on_delete=models.SET_NULL,
    )
    id_cdc = models.OneToOneField(
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.id_registro


class Cdc(models.Model):
    '''
    Definição de atributos para recurso
    carro
    '''

    class Meta:

        db_table = 'cdc'

    id_cdc = models.IntegerField(primary_key=True, unique=True)
    data_criacao = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.id_cdc
