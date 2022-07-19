from asyncio.windows_events import NULL
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from operator import attrgetter

from .models import Livro
from .forms import LivroForm

def exibir_livros_principais(request):
    livros = Livro.objects.all()
    livros_principais = []
    i = 0
    
    for livro in livros:
        if i < 5:
            livros_principais.append(livro)
            i += 1
        else:
            break
    
    livros_principais = sorted(livros_principais, key=attrgetter('titulo'), reverse=False)

    return render(request, 'usuario/home.html', {'livros_principais': livros_principais})

def exibir_novidades(request):
    livros = Livro.objects.all()
    livros = reversed(livros)
    livros_novidades = []
    
    for livro in livros:
        if i < 5:
            livros_novidades.append(livro)
            i += 1
        else:
            break
        
    livros_novidades = sorted(livros_novidades, key=attrgetter('titulo'), reverse=False)

    return render(request, 'usuario/home.html', {'livros_novidades': livros_novidades})

def exibir_livros(request):
    livros = Livro.objects.all()
    lista_livros = []
    i = 0
    
    for livro in livros:
        lista_livros.append(livro)
       

    lista_livros = sorted(lista_livros, key=attrgetter('titulo'), reverse=False)
    return render(request, 'usuario/livro-list.html', {'livros': livros})

def exibir_carrinho(request):
    livros = Livro.objects.all()
    return render(request, 'checkout.html', {'livros': livros})    

livros_no_carrinho = []

def comprar_livros(request, id):
    livro = Livro.objects.get(pk=id)

    livros_no_carrinho.append(livro)
    quantidade_de_itens = 0
    valor_total = 0
    
    for livro in livros_no_carrinho:
        valor_total += livro.valor
        quantidade_de_itens += 1

    return render(request, 'confirmacao.html', {
        'livros': livros_no_carrinho, 
        'valor_total': valor_total, 
        'quantidade_de_itens': quantidade_de_itens
        })

def carrinho(request, id):
    quantidade_de_itens = 0
    valor_total = 0
    
    for livro in livros_no_carrinho:
        valor_total += livro.valor
        quantidade_de_itens += 1

    context = {
        'livros': livros_no_carrinho, 
        'valor_total': valor_total, 
        'quantidade_de_itens': quantidade_de_itens
    }

    return context
   
@login_required
def listar_livros(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        livros = Livro.objects.filter(titulo__icontains=search)
    elif filter:
        livros = Livro.objects.filter(done=filter, user=request.user)
    else:
        lista_livro = Livro.objects.all().order_by('titulo')#.filter(user=request.user)

        paginator = Paginator(lista_livro, 5)

        page = request.GET.get('page')
        livros = paginator.get_page(page)

    return render(request, 'adm/home-adm.html', {'livros': livros})

def detalhar_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return render(request, 'usuario/livro.html', {'livro': livro})

@login_required
def criar_livro(request):
    form = LivroForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_livros')

    return render(request, 'adm/livros-form.html', {'form': form})

@login_required
def atualizar_livro(request, id):
    livro = Livro.objects.get(id=id)
    form  = LivroForm(request.POST or None, instance=livro)

    if form.is_valid():
        form.save()
        return redirect('listar_livros')

    return render(request, 'adm/livros-form.html', {'form': form, 'livro': livro})

@login_required
def excluir_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    livro.delete()

    messages.info(request, 'Livro deletado com sucesso.')

    return redirect('listar_livros')

@login_required
def tabela_livro(request, id):
    livro = get_object_or_404(Livro, pk=id)
    return render(request, 'adm/livro.html', {'livro': livro})