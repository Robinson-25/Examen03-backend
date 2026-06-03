from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import TipoComida, Restaurante
from .serializers import TipoComidaSerializer, RestauranteSerializer

class TipoComidaViewSet(viewsets.ModelViewSet):
    queryset = TipoComida.objects.all()
    serializer_class = TipoComidaSerializer
    parser_classes = [MultiPartParser, FormParser]

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    parser_classes = [MultiPartParser, FormParser]