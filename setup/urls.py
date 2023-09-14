from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clientes.views import *

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)
router.register('produtos', ProdutosViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/compras', ListaComprasPorCliente.as_view()),
    path('produto/<int:pk>/compras', ListaComprasPorProduto.as_view()),
]
