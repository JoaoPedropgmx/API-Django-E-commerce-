from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=9, unique=True)
    celular = models.CharField(max_length=14, unique=True)
    ativo = models.BooleanField()
    ordering = ('nome')

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField(blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default= 'Nenhuma')

    def __str__(self) -> str:
        return self.nome

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return f'Compra nº {self.id}, Cliente: {self.cliente.id}'