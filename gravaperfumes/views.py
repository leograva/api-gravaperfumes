from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from gravaperfumes.models import Estoque, Fabricante,Perfume , Cliente
from gravaperfumes.serializer import ClienteSerializer, FabricanteSerializer, PerfumeSerializer

# Create your views here.
class FabricantesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os fabricantes"""
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ClientesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class PerfumesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os perfumes"""
    queryset = Perfume.objects.all()
    serializer_class = PerfumeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
