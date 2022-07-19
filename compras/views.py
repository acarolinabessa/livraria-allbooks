from django.shortcuts import render, redirect
from .forms import CompraForm
from livros.views import livros_no_carrinho

def novo_cliente(request):
    quantidade_de_itens = 0
    valor_total = 0
    
    for livro in livros_no_carrinho:
        valor_total += livro.valor
        quantidade_de_itens += 1

    form = CompraForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, 'checkout.html', {
        'form': form, 
        'livros': livros_no_carrinho, 
        'valor_total': valor_total, 
        'quantidade_de_itens': quantidade_de_itens
    })