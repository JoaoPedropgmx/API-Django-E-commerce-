from rest_framework import viewsets, filters, generics, serializers, status
from clientes.serializers import ClienteSerializer
from clientes.models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
  

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']

class ProdutosViewSet(viewsets.ModelViewSet):
    """Listando Produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['preco']
    search_fields = ['nome', 'preco']


class ListaComprasPorCliente(generics.ListAPIView):
    def get_queryset(self):
        queryset = Compra.objects.filter( cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCompraPorClienteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaComprasPorProduto(generics.ListAPIView):
    def get_queryset(self):
        queryset = Compra.objects.filter( produto_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCompraPorProdutoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

