from rest_framework import serializers
from .models import TipoComida, Restaurante

class TipoComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoComida
        fields = '__all__'

class RestauranteSerializer(serializers.ModelSerializer):
    tipo_comida_nombre = serializers.CharField(
        source='tipo_comida.nombre', 
        read_only=True
    )
    
    class Meta:
        model = Restaurante
        fields = '__all__'