from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Lista
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url="/user/login/")
def home(request):
    lista = Lista.objects.all().filter(user=request.user).order_by('-id')


    busca = request.GET.get('search')

    if busca:
        lista = lista.filter(title__icontains=busca)

    if request.method == 'POST':
        busca = request.POST.get('search') 
        if busca:
            lista = lista.filter(title__icontains=busca)

        checks = request.POST.getlist('check')
        lista_check = lista.filter(id__in=checks, user=request.user)
        
        for valor in lista_check:
            valor.done = True
            valor.save()
        
        for valor in lista:
            if str(valor.id) not in checks:
                valor.done = False
                valor.save()
        
        return redirect('/')

    paginator = Paginator(lista, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', context={'lista': lista, 'user': request.user, 'logado': request.user.is_authenticated, "page_obj": page_obj})

def adicionar(request):
    if request.method == 'GET':
        return render(request, 'adicionar.html', context={'logado': request.user.is_authenticated})
    else:
        title = request.POST.get('title')
        description = request.POST.get('descricao')
        if not title or not description:
            return redirect('/adicionar')
        
        todo = Lista(user=request.user, title=title, detalhes=description)
        todo.save()
        return redirect('/')
    
def excluir(request, id):
    tarefa = get_object_or_404(Lista, id=id, user=request.user)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('todo_app:home')
    return render(request, 'excluir.html', {'tarefa': tarefa, 'logado': request.user.is_authenticated})

def editar(request, id):
    tarefa = get_object_or_404(Lista, id=id, user=request.user)
    if request.method == "GET":
        return render(request, 'editar.html', {'tarefa': tarefa})
    if request.method == "POST":
        titulo = request.POST.get('title')
        descricao = request.POST.get('descricao')

        tarefa.title = titulo
        tarefa.detalhes = descricao
        tarefa.save()
        return redirect('/')
