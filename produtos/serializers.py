from django_extensions.db import fields
from .models import ProdutoModel
from rest_framework import serializers

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoModel
        fields = ('__all__',)