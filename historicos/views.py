from django.shortcuts import render
from .serializers import HistoricosSerializer
from .services import HistoricoService
from produtos.services import ProdutoService
from django.contrib import messages

_SERVICE = HistoricoService()
_SERVICE_PRODUTO = ProdutoService()


def home_historico(request):
    if request.POST:
        serializer = HistoricosSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
            _SERVICE.salvar_historico(request.POST)
            
    produtos = _SERVICE_PRODUTO.buscar_todos_produtos()
    historicos = _SERVICE.buscar_todos_historicos()
    return render(request, 'home_historico.html', context={"produtos": produtos, "historicos": historicos})
