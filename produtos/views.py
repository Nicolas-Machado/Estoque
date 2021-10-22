from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer

from produtos.serializers import ProdutosSerializer
from .services import ProdutoService
from django.core.paginator import Paginator

_SERVICE = ProdutoService()
def home(request):
    return render(request, 'home.html')
    
def home_produtos(request, produto_id=None):
    if produto_id is not None:
        _SERVICE.remover_contatos_por_id(produto_id)

    produtos = _SERVICE.buscar_todos_produtos()
    paginator = Paginator(produtos, 3)
    page = request.GET.get('p')
    produtos = paginator.get_page(page)
    return render(request, 'home_produtos.html', context={'produtos':produtos})
        

def home_entrada_saida(request):
    return render(request, 'home_entrada_saida.html')

def editar_produto(self, request, produto_id=None):
    if request.method == "GET" and produto_id is not None:
        produto = _SERVICE.buscar_produto_por_id(produto_id)
        return render(request, 'editar.html', context={"produto":produto})
    
    if request.method == "POST" and produto_id is not None:
        produto = _SERVICE.buscar_produto_por_id(produto_id)
        return render(request, 'editar.html', context={"produto":produto}) 
    serializer = ProdutosSerializer(data=request.POST)
    if not serializer.is_valid():
        produto = _SERVICE.buscar_todos_produtos()
        return render(request, 'editar.html', context={"valido":False, "mensagem":"Verifique os campos e tente novamente", "produto":produto})
    produto = _SERVICE.buscar_produto_por_id(id)
    _SERVICE.editar_produto(produto, request.POST)
    return HttpResponseRedirect('/')
    