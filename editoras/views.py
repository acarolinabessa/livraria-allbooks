from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Editora
from .forms import EditoraForm

@login_required
def listar_editoras(request):
    search = request.GET.get('search')
    filter = request.GET.get('filter')

    if search:
        editoras = Editora.objects.filter(nome__icontains=search)
    elif filter:
        editoras = Editora.objects.filter(done=filter, user=request.user)
    else:
        lista_editoras = Editora.objects.all().order_by('nome')

        paginator = Paginator(lista_editoras, 5)

        page = request.GET.get('page')
        editoras = paginator.get_page(page)

    return render(request, 'editoras-list.html', {'editoras': editoras})

def detalhar_editora(request, id):
    editora = get_object_or_404(Editora, pk=id)
    return render(request, 'editora.html', {'editora': editora})

@login_required
def criar_editora(request):
    form = EditoraForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_editoras')

    return render(request, 'editoras-form.html', {'form': form})

@login_required
def atualizar_editora(request, id):
    editora = Editora.objects.get(id=id)
    form  = EditoraForm(request.POST or None, instance=editora)

    if form.is_valid():
        form.save()
        return redirect('listar_editoras')

    return render(request, 'editoras-form.html', {'form': form, 'editora': editora})

@login_required
def excluir_editora(request, id):
    editora = get_object_or_404(Editora, pk=id)
    editora.delete()

    messages.info(request, 'Editora deletada com sucesso.')

    return redirect('listar_editoras')

@login_required
def tabela_editora(request, id):
    editora = get_object_or_404(Editora, pk=id)
    return render(request, 'editora.html', {'editora': editora})