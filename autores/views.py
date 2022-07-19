from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from operator import attrgetter
from .models import Autor
from .forms import AutorForm

@login_required
def listar_autores(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        autores = Autor.objects.filter(nome__icontains=search)
    elif filter:
        autores = Autor.objects.filter(done=filter, user=request.user)
    else:
        lista_autores = Autor.objects.all().order_by('nome')

        paginator = Paginator(lista_autores, 5)

        page = request.GET.get('page')
        autores = paginator.get_page(page)

    return render(request, 'autores-list.html', {'autores': autores})

def detalhar_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)
    return render(request, 'autor.html', {'autor': autor})

@login_required
def criar_autor(request):
    form = AutorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_autores')

    return render(request, 'autores-form.html', {'form': form})

@login_required
def atualizar_autor(request, id):
    autor = Autor.objects.get(id=id)
    form  = AutorForm(request.POST or None, instance=autor)

    if form.is_valid():
        form.save()
        return redirect('listar_autores')

    return render(request, 'autores-form.html', {'form': form, 'autor': autor})

@login_required
def excluir_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)
    autor.delete()

    messages.info(request, 'Autor deletado com sucesso.')

    return redirect('listar_autores')

@login_required
def tabela_autor(request, id):
    autor = get_object_or_404(Autor, pk=id)
    return render(request, 'autor.html', {'autor': autor})