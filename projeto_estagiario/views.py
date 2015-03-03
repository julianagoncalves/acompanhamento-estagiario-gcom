from django.shortcuts import render
from django.http import HttpResponse
from forms import AtividadeForm

# Create your views here.
def index(request):
    form = AtividadeForm()
    return render(request, 'projeto_estagiario/index.html', {
        'form': form,
    })
