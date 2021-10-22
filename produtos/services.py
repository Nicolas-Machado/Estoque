import uuid
from .models import ProdutoModel

class ProdutoService():
    
    def buscar_todos_produtos(self) -> list[ProdutoModel]:
        return ProdutoModel.objects.all()

    def buscar_produto_por_id(self, id:uuid) -> ProdutoModel:
        return ProdutoModel.objects.filter(id=id).first()

    def buscar_produto_por_codigo(self, codigo:str) -> ProdutoModel:
        return ProdutoModel.objects.filter(codigo=codigo).first()
    
    def remover_contatos_por_id(self, id:uuid) -> None:
        return ProdutoModel.objects.filter(id=id).delete()

    def editar_produto(produto:ProdutoModel, data:dict,) -> None:
        produto.nome = data['nome']
        produto.codigo= data['codigo']
        produto.save()