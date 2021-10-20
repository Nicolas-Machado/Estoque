from django.http import request
from django.shortcuts import render
from .services import ProdutoService

_SERVICE = ProdutoService()
def home(request):
    return render(request, 'home.html')
    
def home_produtos(request):
    produtos = _SERVICE.buscar_todos_produtos()
    return render(request, 'home_produtos.html', context={"produtos":produtos})
        

def home_entrada_saida(request):
    return render(request, 'home_entrada_saida.html')

