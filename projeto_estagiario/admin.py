from django.contrib import admin
from projeto_estagiario.models import Atividade
from projeto_estagiario.models import Tarefa
from projeto_estagiario.models import Usuario
from projeto_estagiario.models import PerfilEstagiario

admin.site.register(Atividade)

admin.site.register(Tarefa)

admin.site.register(Usuario)

admin.site.register(PerfilEstagiario)