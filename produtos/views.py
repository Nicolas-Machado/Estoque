import uuid
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.contrib import messages
from produtos.serializers import ProdutosSerializer
from .services import ProdutoService
from django.core.paginator import Paginator
from .serializers import ProdutosSerializer

_SERVICE = ProdutoService()


def home(request):
    return render(request, 'home.html')


def home_produtos(request, id:uuid=None):
    if id is not None:
        _SERVICE.remover_produtos_por_id(id)
    elif request.method == "POST" and id is None:
        serializer = ProdutosSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
                serializer.save()
    produtos = _SERVICE.buscar_todos_produtos()
    paginator = Paginator(produtos, 5)
    page = request.GET.get('p')
    produtos = paginator.get_page(page)
    return render(request, 'home_produtos.html', context={"produtos":produtos})


def home_entrada_saida(request):
    return render(request, 'home_entrada_saida.html')


def home_editar_produto(request, id:uuid):
    produto = _SERVICE.buscar_produto_por_id(id)

    if request.method == "GET":
        return render(request, 'home_editar.html', context={"produto":produto})

    message = _SERVICE.editar_produto(produto, request.POST)
    if message is not None:
         messages.error(request, message)
         messages.warning(request, "ERROR")
         messages.info(request, "INFO")
         return render(request, template_name='home_editar.html', context={"produto":produto, "message":message})
    messages.success(request, "Salvo com sucesso")
    return render(request, template_name='home_editar.html', context={"produto":produto, "message":message})
