from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Contato
from .forms import ProdutoForm, ContatoForm
from django.utils import timezone


# Create your views here.
def index(request):
    lista_categorias = Categoria.objects.all()

    dados = {
        'Categorias': lista_categorias
    }
    return render(request, 'index.html', dados)


def lista_produtos(request):
    lista_produtos = Produto.objects.filter(ativado=True)
    lista_categorias = Categoria.objects.all()

    dados = {
        'Produtos': lista_produtos,
        'Categorias': lista_categorias
    }
    return render(request, 'produtos.html', dados)


def produto_detalhes(request, slug):
    lista_categorias = Categoria.objects.all()
    produto = Produto.objects.get(slug=slug)

    dados = {
        'Produtos': produto,
        'Categorias': lista_categorias
    }
    return render(request, 'produto.html', dados)


def lista_produtos_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    produto = Produto.objects.filter(categoria=categoria)
    categoria = Categoria.objects.all()

    dados = {
        'Categorias': categoria,
        'Produtos': produto,

    }

    return render(request, 'categoria.html', dados)


def buscar(request):
    lista_produtos = Produto.objects.order_by('-data_publicacao')

    if 'buscar' in request.GET:
        
        buscar_produto = request.GET['buscar']
        if buscar:
            lista_produtos = lista_produtos.filter(nome_produto__icontains=buscar_produto)

    dados = {

        'Produtos': lista_produtos
    }

    return render(request, 'buscar.html', dados)


def contato(request):
    categoria = Categoria.objects.all()
    
    if request.method == 'POST':
        form = ContatoForm(request.POST)

        if form.is_valid():
            contato = Contato()
            contato.nome = form.cleaned_data['nome']
            contato.email = form.cleaned_data['email']
            contato.mensagem = form.cleaned_data['mensagem']
            contato.save()

            messages.success(request, "Mensagem enviado com sucesso")            
            return redirect('contato')
             
    

    else:

        form = ContatoForm()

        return render(request, 'contato.html', {'form': form})


""" daqui p/ baixo views p/ ADMIN """



def adicionar_produto(request):
    form_class = ProdutoForm
    form = form_class(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form = ProdutoForm(request.POST, request.FILES)
            f = form.save(commit=False)
            #f.data_publicacao = timezone.now()
            #f.data_alteracao = timezone.now()
            f.usuario = request.user
            f.save()

            return redirect('dashboard')

    else:
        form = ProdutoForm

    dados = {
        'form': form
    }
    return render(request, 'adicionar-admin.html', dados)


def editar_produto(request, slug):
    form_class = ProdutoForm
    form = form_class(request.POST or None)
    produto = get_object_or_404(Produto, slug=slug)  # verifica se existe esse obj no BD

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            f = form.save(commit=False)
            f.data_criacao = timezone.now()
            f.data_alteracao = timezone.now()
            f.save()
            return redirect('dashboard')

    else:
        form = ProdutoForm(instance=produto)

    dados = {
        'form': form

    }

    return render(request, 'editar-admin.html', dados)


def excluir_produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    if produto:
        produto.delete()

    return redirect('dashboard')


def produto_detalhes_admin(request, slug):
    produto = Produto.objects.get(slug=slug)

    dados = {
        'Produtos': produto

    }
    print(produto)
    return render(request, 'produto-detalhes-admin.html', dados)
