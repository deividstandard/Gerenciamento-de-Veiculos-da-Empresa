from .models import Carro
from .models import Registro
from .models import Cdc
from rest_framework import serializers


class SerializadorCarro(serializers.ModelSerializer):

    class Meta:

        model = Carro
        fields = '__all__'


class SerializadorRegistro(serializers.ModelSerializer):

    class Meta:

        model = Registro
        fields = '__all__'


class SerializadorCdc(serializers.ModelSerializer):

    class Meta:

        model = Cdc
        fields = '__all__'
