from rest_framework import generics
from .models import *
from .serializers import *

class ParadaList(generics.ListCreateAPIView):

    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer


'''class ParadaList(generics.ListCreateAPIView):
    serializer_class = ParadaSerializer

    def get_queryset(self):
        queryset = Parada.objects.all()
        linha = self.request.query_params.get('linha', None)
        if linha is not None:
            queryset = queryset.filter(linhas__parada=linha)
            
        return queryset'''    

class ParadaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer
class LinhaList(generics.ListCreateAPIView):

    queryset = Linha.objects.all()
    serializer_class = LinhaSerializer

class LinhaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Linha.objects.all()
    serializer_class = LinhaSerializer

class VeiculoList(generics.ListCreateAPIView):

    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class VeiculoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class PosicaoVeiculoList(generics.ListCreateAPIView):

    queryset = PosicaoVeiculo.objects.all()
    serializer_class = PosicaoVeiculoSerializer

class PosicaoVeiculoDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = PosicaoVeiculo.objects.all()
    serializer_class = PosicaoVeiculoSerializer