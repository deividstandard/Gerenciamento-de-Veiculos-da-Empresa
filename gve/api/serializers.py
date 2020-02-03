from .models import CarroModel
from .models import RegistroModel
from .models import CdcModel
from rest_framework import serializers


class SerializadorCarro(serializers.ModelSerializer):

    class Meta:

        model = CarroModel
        fields = '__all__'


class SerializadorRegistro(serializers.ModelSerializer):

    class Meta:

        model = RegistroModel
        fields = '__all__'


class SerializadorCdc(serializers.ModelSerializer):

    class Meta:

        model = CdcModel
        fields = '__all__'
