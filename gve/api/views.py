from .models import Cdc
from .models import Carro
from .models import Registro

from rest_framework import viewsets
from rest_framework import generics
from .serializers import SerializadorCdc
from .serializers import SerializadorCarro
from .serializers import SerializadorRegistro

# Create your views here.


class Carro(viewsets.ModelViewSet):

    queryset = Carro.objects.all()
    serializer_class = SerializadorCarro

class Registro(viewsets.ModelViewSet):

    queryset = Registro.objects.all()
    serializer_class = SerializadorRegistro

class Cdc(viewsets.ModelViewSet):

    queryset = Cdc.objects.all()
    serializer_class = SerializadorCdc
