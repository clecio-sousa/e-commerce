from django.contrib import admin
from .models import Produto, Categoria, Contato


# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome_produto', 'preco_produto', 'ativado']
    list_display_links = ['nome_produto']
    search_fields = ['nome_produto']
    prepopulated_fields = {'slug': ('nome_produto',)}




admin.site.register(Produto, ProdutoAdmin)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_categoria', 'slug')
    list_filter = ['nome_categoria']
    prepopulated_fields = {'slug': ('nome_categoria',)}


admin.site.register(Categoria, CategoriaAdmin)

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'mensagem', 'enviado_em')

admin.site.register(Contato, ContatoAdmin)