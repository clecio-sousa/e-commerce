from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from produtos.models import Produto
# Create your views here.


def cadastro(request):
    if request.method == 'POST':
        # atributo name no template
        nome = request.POST['nome']
        email = request.POST['email']
        senha1 = request.POST['senha1']
        senha2 = request.POST['senha2']
        if not nome.strip():  # se nome nao estah vazio
            return redirect('cadastro')

        if not email.strip():
            print("email nao pode ficar em branco")
            return redirect('cadastro')

        if senha1 != senha2:
            messages.error(request, 'As senhas não são iguais.')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists(): # verifica se jah existe usuario com o email
            messages.error(request, 'usuário já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha1)  # cria um novo usuario
        user.save()  # salva no BD
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('login')
    else:
        return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "": # vrifica se os campos estao em branco
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() # verificar propriedades
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print("Login realizado com sucesso!!")
            print(nome)

        return redirect('dashboard')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        produtos = Produto.objects.order_by('-data_publicacao').filter(usuario=request.user)

        dados = {
            'Produtos': produtos
        }
        return render(request, 'dashboard.html', dados)
    else:
        return redirect('index')
