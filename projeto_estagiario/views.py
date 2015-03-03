from django.shortcuts import render
from django.http import HttpResponse
from forms import AtividadeForm, TarefaForm

# Create your views here.
def index(request):
    atividade_form = AtividadeForm()
    tarefa_form = TarefaForm()
    return render(request, 'projeto_estagiario/index.html', {
        'atividade_form': atividade_form,
        'tarefa_form': tarefa_form,
    })

def perfil(request):
    return render(request, 'projeto_estagiario/perfil.html',{
    })
