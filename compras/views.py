from django.shortcuts import render, redirect
from .forms import CompraForm

def novo_cliente(request):
    form = CompraForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request, 'checkout.html', {'form': form})