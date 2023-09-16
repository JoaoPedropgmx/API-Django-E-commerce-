from rest_framework import viewsets, filters, generics, status
from rest_framework.response import Response
from clientes.serializers import ClienteSerializer
from clientes.models import *
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    filterset_fields = ['ativo']

    def create(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = Response(serializer.data, status=status.HTTP_201_CREATED)
                id = str(serializer.data['id'])
                response['Location'] = request.build_absolute_uri() + id
                return response

    

class ProdutosViewSet(viewsets.ModelViewSet):
    """Listando Produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['preco']
    search_fields = ['nome', 'preco']

    def create(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                response = Response(serializer.data, status=status.HTTP_201_CREATED)
                id = str(serializer.data['id'])
                response['Location'] = request.build_absolute_uri() + id
                return response


class ListaComprasPorCliente(generics.ListAPIView):
    def get_queryset(self):
        queryset = Compra.objects.filter( cliente_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCompraPorClienteSerializer

class ListaComprasPorProduto(generics.ListAPIView):
    def get_queryset(self):
        queryset = Compra.objects.filter( produto_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCompraPorProdutoSerializer
