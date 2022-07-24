from rest_framework import serializers
from gravaperfumes.models import Estoque, Fabricante,Perfume,Cliente,Venda

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PerfumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfume
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'