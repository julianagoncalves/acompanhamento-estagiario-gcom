from django.forms import Form, ModelForm, BooleanField, DateField, TextInput, CheckboxInput, DateInput, HiddenInput, Textarea, Select, RadioSelect

from models import Atividade, Tarefa


class AtividadeForm(ModelForm):

    class Meta:
        model = Atividade

        fields = [
            'descricao_historia',
            'conhecimento_adquirido',
            'material_apoio',
            'gestor_estagiario',
            'tutor_estagiario',
            'comentario_tutor',
            'comentario_estagiario',
            'data_inicio',
            'data_fim'
        ]

        widgets = {
            'descricao_historia': Textarea(attrs={'rows': 3}),
            'conhecimento_adquirido': Textarea(attrs={'rows': 3}),
            'material_apoio': Textarea(attrs={'rows': 3}),
            'gestor_estagiario': TextInput(attrs={'maxlength': 80}),
            'tutor_estagiario': TextInput(attrs={'maxlength': 80}),
            'comentario_tutor': Textarea(attrs={'rows': 3}),
            'comentario_estagiario': Textarea(attrs={'rows': 3}),
            'data_inicio': DateInput(format='%d/%m/%Y', attrs={'tabindex': 4, 'maxlength': 10}),
            'data_fim': DateInput(format='%d/%m/%Y', attrs={'tabindex': 4, 'maxlength': 10}),
        }


class TarefaForm(ModelForm):

    class Meta:
        model = Tarefa

        fields = ['descricao_tarefa', 'principais_dificuldades', 'status']

        widgets = {
            'descricao_tarefa': TextInput(attrs={'maxlength': 80}),
            'principais_dificuldades': Textarea(attrs={'rows': 3}),
            'status': RadioSelect(),
        }
