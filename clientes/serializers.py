import re
from rest_framework import serializers
from clientes.models import *
from validate_docbr import CPF

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate_cpf(self, numero_cpf):
        cpf = CPF()
        if not cpf.validate(numero_cpf):
            raise serializers.ValidationError("O CPF é Inválido")
        return numero_cpf
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("O nome deve possuir somente characteres alfabéticos")
        return nome
    def validate_rg(self, rg):
        if len(rg) != 9 or not rg.isnumeric():
            raise serializers.ValidationError("RG inválido")
        return rg
    def validate_celular(self, celular):
        model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(model, celular)
        if not resposta:
            raise serializers.ValidationError("Celular inválido")
        return celular

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class CompraSerializer(serializers.ModelSerializer):
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    produto = serializers.ReadOnlyField(source='produto.nome')
    class Meta:
        model = Compra
        fields = ['id', 'cliente', 'produto']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ListaCompraPorClienteSerializer(serializers.ModelSerializer):
    produto = serializers.ReadOnlyField(source='produto.nome')
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    id_produto = serializers.ReadOnlyField(source='produto.id')
    class Meta:
        model = Compra
        fields = ['id','produto', 'id_produto', 'cliente']

class ListaCompraPorProdutoSerializer(serializers.ModelSerializer):
    produto = serializers.ReadOnlyField(source='produto.nome')
    cliente = serializers.ReadOnlyField(source='cliente.nome')
    id_produto = serializers.ReadOnlyField(source='produto.id')
    class Meta:
        model = Compra
        fields = ['id','produto', 'id_produto', 'cliente']