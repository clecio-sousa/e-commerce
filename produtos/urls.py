from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos', views.lista_produtos, name='produtos'),
    path('produto/<slug:slug>', views.produto_detalhes, name='produto_detalhes'),
    path('categoria/<slug:slug>', views.lista_produtos_categoria, name='categoria'),
    path('contato', views.contato, name='contato'),
    path('buscar', views.buscar, name='buscar'),
    path('adicionar-produto', views.adicionar_produto, name='adicionar_produto'),
    path('editar-produto/<slug:slug>', views.editar_produto, name='editar_produto'),
    path('excluir-produto/<slug:slug>', views.excluir_produto, name='excluir_produto'),
    path('produto-detalhes/<slug:slug>', views.produto_detalhes_admin, name='produto_detalhes_admin')

]

