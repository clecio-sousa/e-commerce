from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome_categoria


class Produto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nome_produto = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    descricao_produto = models.TextField(max_length=100)
    preco_produto = models.DecimalField(max_digits=9, decimal_places=2)
    imagem_produto = models.ImageField(upload_to='img', blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False, null=False)

    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado')
    )

    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')

    data_publicacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    ativado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_produto


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensagem = models.TextField(max_length=200)
    enviado_em = models.DateTimeField(auto_now=True, blank=True)

    ASSUNTO = (
        ('sugestao', 'Sugestão'),
        ('reclamacao', 'Reclamação')
    )
    assunto = models.CharField(max_length=10,
                               choices=ASSUNTO,
                               default='sugestao')

    def __str__(self):
        return self.nome
