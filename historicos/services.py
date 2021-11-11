from django.http import request
from .models import HistoricoModel
from produtos.services import ProdutoService
from django.contrib import messages
_SERVICE_PRODUTO = ProdutoService()

class HistoricoService():

    def salvar_historico(self, data:dict):
        produto = _SERVICE_PRODUTO.buscar_produto_por_id(data.get("produto_id"))
        historico = HistoricoModel(
            produto_id=produto,
            funcionario=data.get("funcionario"),
            tipo=data.get("tipo"),
            quantidade=data.get("quantidade"),
            observacao=data.get("observacao"),
        )
        historico.save()

    def buscar_todos_historicos(self):
        return HistoricoModel.objects.all() 