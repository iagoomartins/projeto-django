from django.shortcuts import render, redirect
from usuarios.forms import LoginForm, RegistroForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Views de Login, Cadastro e Logout
def login(request):
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        # validação do formulário
        if form.is_valid():

            nome = form['nome_login'].value()
            senha = form['senha'].value()

            # autenticação do usuário
            usuario = auth.authenticate(request, username=nome, password=senha)

            # fazer login de fato
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, 'Login efetuado com sucesso!')
                return redirect('home')
            # se der MERDA, volta para a página de login
            else:
                messages.error(request, 'Usuário ou senha incorretos.')
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):

    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)

        # validação do formulário
        if form.is_valid():
        # validação de senha
            if form['senha_1'].value() != form['senha_2'].value():
                # caso a senha esteja incorreta, exibe mensagem de erro, 
                # volta para a página de cadastro para o usuario tentar novamente
                messages.error(request, 'Senhas não conferem.')
                return redirect('cadastro')
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()
            
            # verificar se já existe um usuário com o mesmo nome de login
            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe.')
                return redirect('cadastro')

            # criar usuário
            usuario = User.objects.create_user(
                username=nome, 
                email=email, 
                password=senha)
            usuario.save()
            messages.success(request, 'Usuário criado com sucesso!')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucesso. Volte sempre!')
    return redirect('login')