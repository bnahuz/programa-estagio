from rest_framework import generics
from .models import *
from .serializers import *

class ParadaList(generics.ListCreateAPIView):

    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer

class LinhaList(generics.ListCreateAPIView):

    queryset = Linha.objects.all()
    serializer_class = LinhaSerializer

class VeiculoList(generics.ListCreateAPIView):

    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class PosicaoVeiculoList(generics.ListCreateAPIView):

    queryset = PosicaoVeiculo.objects.all()
    serializer_class = PosicaoVeiculoSerializer