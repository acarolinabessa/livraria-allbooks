from django.urls import path
from .views import listar_editoras, criar_editora, atualizar_editora, excluir_editora, tabela_editora

urlpatterns = [
    path('editora-list', listar_editoras, name='listar_editoras'),
    path('editora-new', criar_editora, name='criar_editora'),
    path('editora-update/<int:id>', atualizar_editora, name='atualizar_editora'),
    path('editora-delete/<int:id>', excluir_editora, name='excluir_editora'),
    path('editora-detail/<int:id>', tabela_editora, name='tabela_editora'),
]