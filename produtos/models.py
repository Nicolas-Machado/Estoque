from django.db import models
import uuid
from django_extensions.db.models import TimeStampedModel

class ProdutoModel(TimeStampedModel):
    id = models.UUIDField(
        db_column="ID",
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        unique=True
    )

    nome = models.CharField(
        db_column="NOME",
        max_length=100
    )

    codigo = models.CharField(
        db_column="CODIGO",
        max_length=20,
        unique=True
    )

    def __str__(self) -> str:
        return self.nome

    class Meta:
        db_table = 'PRODUTO'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
