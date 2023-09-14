from django.contrib import admin
from clientes.models import *

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email','cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'cpf')
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 25

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'categoria')
    list_per_page = 25

class Categorias(admin.ModelAdmin):
    search_fields =  ('nome',)
    list_per_page = 25

class Compras(admin.ModelAdmin):
    list_per_page = 25

admin.site.register(Cliente, Clientes)
admin.site.register(Categoria, Categorias)
admin.site.register(Produto, Produtos)
admin.site.register(Compra, Compras)


