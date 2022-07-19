from django.urls import path
from .views import listar_autores, criar_autor, atualizar_autor, excluir_autor, detalhar_autor, tabela_autor

urlpatterns = [
    path('autor-list', listar_autores,name='listar_autores'),
    path('autor-new', criar_autor,name='criar_autor'),
    path('autor-update/<int:id>', atualizar_autor,name='atualizar_autor'),
    path('autor-delete/<int:id>', excluir_autor,name='excluir_autor'),
    path('autor/<int:id>', detalhar_autor, name='detalhar_autor'),
    path('autor-detail/<int:id>', tabela_autor, name='tabela_autor'),
]