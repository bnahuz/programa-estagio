from .models import *
from .serializers import *
from rest_framework import generics
from django_filters import rest_framework as filters


class ParadaList(generics.ListCreateAPIView): 

    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer  

class ParadaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer
class LinhaList(generics.ListCreateAPIView):

    queryset = Linha.objects.all()
    serializer_class = LinhaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class LinhaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Linha.objects.all()
    serializer_class = LinhaSerializer

class VeiculoList(generics.ListCreateAPIView):

    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
    
class VeiculoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class PosicaoVeiculoList(generics.ListCreateAPIView):

    queryset = PosicaoVeiculo.objects.all()
    serializer_class = PosicaoVeiculoSerializer

class PosicaoVeiculoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = PosicaoVeiculo.objects.all()
    serializer_class = PosicaoVeiculoSerializer