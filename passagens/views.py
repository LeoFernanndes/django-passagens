from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def index(request):
    form = forms.PassagemForms()
    contexto = {
        'form': form
    }

    return render(request, 'index.html', contexto)

def minha_consulta(request):
    if request.method == 'POST':
        form = forms.PassagemForms(request.POST)
        contexto = {
            'form': form
        }

        return render(request, 'minha_consulta.html', contexto)

    if request.method == "GET":
        return redirect('index')
    
   