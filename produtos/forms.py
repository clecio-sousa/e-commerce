from django import forms
from .models import Produto, Contato

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        exclude = ('usuario', 'data_publicacao', 'data_alteracao')


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']
        exclude = ('enviado_em',)


