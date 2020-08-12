from rest_framework import serializers
from .models import *

class ParadaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Parada
        fields = '__all__'

class LinhaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Linha
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Veiculo
        fields = '__all__'

class PosicaoVeiculoSerializer(serializers.ModelSerializer):

    class Meta:

        model = PosicaoVeiculo
        fields = '__all__'