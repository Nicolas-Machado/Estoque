import uuid
from django.db import models
from django.db.models.fields import TimeField
from django.db.models.fields.related import ForeignKey
from django_extensions.db.models import TimeStampedModel

from produtos.models import ProdutoModel

class HistoricoModel(TimeStampedModel):
    id = models.UUIDField(
        db_column="ID",
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        unique=True
    )
    produto_id = models.ForeignKey(
        ProdutoModel,
        on_delete=models.CASCADE
    )

    data = models.DateField(auto_now=True)

    funcionario = models.CharField(
        db_column="FUNCIONARIO",
        max_length=50
    )

    tipo = models.CharField(
        max_length=30
    )

    quantidade = models.PositiveSmallIntegerField(
        default=None
    )

    observacao = models.TextField(
        default=None)

    class Meta:
        db_table = "HISTORICO"
        verbose_name = "Historico"
        verbose_name_plural = "Historicos"
