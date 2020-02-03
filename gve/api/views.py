from .models import CdcModel
from .models import CarroModel
from .models import RegistroModel

from rest_framework import viewsets
from rest_framework import generics
from .serializers import SerializadorCdc
from .serializers import SerializadorCarro
from .serializers import SerializadorRegistro

# Create your views here.


class CarroViewSet(viewsets.ModelViewSet):

    queryset = CarroModel.objects.all()
    serializer_class = SerializadorCarro


class RegistroViewSet(viewsets.ModelViewSet):

    queryset = RegistroModel.objects.all()
    serializer_class = SerializadorRegistro


class CdcViewSet(viewsets.ModelViewSet):

    queryset = CdcModel.objects.all()
    serializer_class = SerializadorCdc
