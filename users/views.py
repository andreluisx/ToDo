from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'logado': request.user.is_authenticated})
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if User.objects.filter(username=username).exists():
            messages.add_message(request, constants.ERROR, 'Esse nome de usuário já existe!')
            return redirect('/user/')
        
        if len(password) < 3:
            messages.add_message(request, constants.ERROR, 'A senha deve ter 3 ou mais dígitos!')
            return redirect('/user/')
        
        if User.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Esse email já está em uso!')
            return redirect('/user/')

        usuario = User(first_name=name, email=email, username=username)
        usuario.set_password(password)  # Criptografar a senha
        usuario.save()
        return redirect('/user/login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', context={'logado': request.user.is_authenticated})
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect('/')
        
        messages.add_message(request, constants.ERROR, 'Credenciais inválidas!')
        return redirect('/user/login')
        
def sair(request):
    auth.logout(request)
    return redirect('/user/login')
