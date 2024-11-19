# serializers.py
from rest_framework import serializers
from .models import Categoria, Producto, Cliente, Factura, ItemFactura, Configuracion

from rest_framework import serializers
from .models import Producto, Categoria  # Adjust the import based on your project structure

from rest_framework import serializers
from .models import Producto, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']

class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())  # Acepta solo el ID de la categoría

    class Meta:
        model = Producto
        fields = ['id', 'codigo', 'nombre', 'categoria', 'precio', 'stock']

    def update(self, instance, validated_data):
        # Actualiza los demás campos
        instance.codigo = validated_data.get('codigo', instance.codigo)
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.stock = validated_data.get('stock', instance.stock)

        # Guardar la instancia actualizada
        instance.save()
        return instance
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'ci', 'nombre', 'email', 'telefono', 'direccion']

class ItemFacturaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    
    class Meta:
        model = ItemFactura
        fields = ['id', 'producto', 'cantidad', 'precio']

class FacturaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()
    items = ItemFacturaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Factura
        fields = ['id', 'numero', 'cliente', 'total', 'iva', 'creada_en', 'items']

class ConfiguracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion
        fields = ['id', 'iva_porcentaje', 'tiempo_respuesta_sla']