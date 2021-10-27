from django.urls import path
from django.urls import path
from .views import home, home_editar_produto, home_produtos, home_entrada_saida


urlpatterns = [
    path('', home, name="home"),
    path('produtos/', home_produtos , name="produtos"),
    path('entrada_saida/', home_entrada_saida , name="entrada_saida" ),
    path('deletar/<uuid:id>', home_produtos , name="deletar"),
    path('editar/<uuid:id>/', home_editar_produto , name="editar"),
]
