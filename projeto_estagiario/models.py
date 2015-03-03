from django.db import models

TIPOS_STATUS = (
        ('Concluida', 'Concluida'),
        ('Em Andamento', 'Em Andamento'),
        ('Parada', 'Parada'),
)


class Atividade(models.Model):
    id = models.AutoField(primary_key=True, db_column="atividade_id")
    descricao_historia = models.CharField(max_length=100, db_column="descricao_historia_txt", verbose_name='Descricao Historia')
    conhecimento_adquirido = models.CharField(max_length=100, db_column="conhecimento_adquirido_txt", verbose_name='Conhecimentos Adquiridos')
    material_apoio = models.CharField(max_length=100, db_column="material_apoio_txt", verbose_name='Material Apoio')
    gestor_estagiario = models.CharField(max_length=20, db_column="gestor_estagiario_txt", verbose_name='Gestor Estagiario')
    tutor_estagiario = models.CharField(max_length=200, db_column="tutor_estagiario_txt", verbose_name='Tutor Estagiario')
    comentario_tutor = models.CharField(max_length=200, db_column="comentario_tutor_txt", verbose_name='Comentarios Tutor')
    comentario_estagiario = models.CharField(max_length=200, db_column="comentario_estagiario_txt", verbose_name='Comentarios Estagiario')
    data_inicio = models.DateTimeField('Data Inicio')
    data_fim = models.DateTimeField('Data Fim')

    class Meta:
        db_table = "acompanhamento_estagiario_atividade"
        verbose_name = u'Atividade'
        verbose_name_plural = u'Atividades'

class Tarefa(models.Model):
    id = models.AutoField(primary_key=True, db_column="tarefa_id")
    id_atividade = models.ForeignKey(Atividade)
    descricao_tarefa = models.CharField(max_length=200, db_column="descricao_tarefa_txt", verbose_name='Descricao Tarefa')
    principais_dificuldades = models.CharField(max_length=100, db_column="principais_dificuldades_txt", verbose_name='Principais Dificuldades')

    status = models.CharField(max_length=15, db_column="status_txt", verbose_name='Status', choices=TIPOS_STATUS)

    class Meta:
        db_table = "acompanhamento_estagiario_tarefa"
        verbose_name = u'Tarefa'
        verbose_name_plural = u'Tarefas'

class Usuario(models.Model):
    id = models.AutoField(primary_key=True, db_column="usuario_id")
    email = models.CharField(max_length=30, db_column="email_txt", verbose_name='Email')
    tipo_usuario = models.CharField(max_length=1, db_column="tipo_usuario_txt", verbose_name='Tipo Usuario')
    senha = models.CharField(max_length=20, db_column="senha_txt", verbose_name='Senha')

    class Meta:
        db_table = "acompanhamento_estagiario_usuario"

class PerfilEstagiario(models.Model):
    id = models.AutoField(primary_key=True, db_column="perfil_estagiario_id")
    nome = models.CharField(max_length=50, db_column="nome_txt", verbose_name='Nome')
    data_nascimento = models.DateTimeField('Data Nascimento')
    instituicao_ensino = models.CharField(max_length=50, db_column="instituicao_ensino_txt", verbose_name='Instituicao de Ensino')
    curso = models.CharField(max_length=50, db_column="curso_txt", verbose_name='Curso')
    periodo_curso = models.IntegerField(db_column="periodo_txt", verbose_name='Periodo Curso')
    previsao_formatura = models.DateTimeField('Previsao Formatura')
    curso_extra = models.CharField(max_length=900, db_column="curso_extra_txt", verbose_name='Cursos Extras')
    curso_rh = models.CharField(max_length=900, db_column="curso_rh_txt", verbose_name='Cursos RH')

    class Meta:
        db_table = "acompanhamento_estagiario_perfil_estagiario"

