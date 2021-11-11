from django.db.models import fields
from .models import HistoricoModel
from rest_framework import serializers
from produtos.services import ProdutoService

_SERVICE_PRODUTO = ProdutoService()

class HistoricosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoModel
        fields = ('id', 'produto_id', 'funcionario', 'tipo', 'observacao')