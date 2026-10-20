from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('novoItem/', views.novo_item, name='novo-item'),
    path('novoItemSucesso/', views.novo_item_sucesso, name='novo_item_sucesso'),
    path('alterarItem/<int:codigo_item>', views.alterar_item, name='alterar_item'),
    path('excluirItem/<int:codigo_item>', views.excluir_item, name='excluir_item'),
    path('buscar/', views.buscar_item, name='buscar_item'),
]
