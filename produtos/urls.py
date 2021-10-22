from django.urls import path
from django.urls import path
from .views import editar_produto, home, home_produtos, home_entrada_saida


urlpatterns = [
    path('', home, name="home"),
    path('produtos/', home_produtos , name="produtos"),
    path('entrada_saida/', home_entrada_saida , name="entrada_saida" ),
    path('deletar/<uuid:produto_id>', home_produtos , name="deletar"),
    path('editar/<uuid:produto_id>', editar_produto , name="editar"),
    path('deletar/salvar', editar_produto , name="editar")
]
