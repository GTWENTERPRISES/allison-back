from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Categoria, Producto, Cliente, Factura, ItemFactura, Configuracion
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, FacturaSerializer, ItemFacturaSerializer, ConfiguracionSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class ItemFacturaViewSet(viewsets.ModelViewSet):
    queryset = ItemFactura.objects.all()
    serializer_class = ItemFacturaSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer