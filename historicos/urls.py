from django.urls import path
from .views import home_historico

urlpatterns = [
    path('historico', home_historico, name="historico"),
]
