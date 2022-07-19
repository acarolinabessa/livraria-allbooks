from django.urls import path
from .views import exibir_livros_principais, exibir_novidades, exibir_livros, exibir_carrinho, detalhar_livro, listar_livros, criar_livro, atualizar_livro, excluir_livro, tabela_livro, comprar_livros

urlpatterns = [
    path('', exibir_livros_principais, name='exibir_livros_principais'),
    path('', exibir_novidades, name='exibir_novidades'),
    path('livro/all', exibir_livros, name='exibir_livros'),
    path('livro/carrinho', exibir_carrinho, name='exibir_carrinho'),
    path('livro/<int:id>', detalhar_livro, name='detalhar_livro'),
    # Área do ADM
    path('livro-list', listar_livros, name='listar_livros'),
    path('livro-new', criar_livro, name='criar_livro'),
    path('livro-update/<int:id>', atualizar_livro, name='atualizar_livro'),
    path('livro-delete/<int:id>', excluir_livro, name='excluir_livro'),
    path('livro-detail/<int:id>', tabela_livro, name='tabela_livro'),
    path('livro-comprar/<int:id>', comprar_livros, name='comprar_livros'),
]