# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'atividade_id')),
                ('descricao_historia', models.CharField(max_length=100, verbose_name=b'Descricao Historia', db_column=b'descricao_historia_txt')),
                ('conhecimento_adquirido', models.CharField(max_length=100, verbose_name=b'Conhecimentos Adquiridos', db_column=b'conhecimento_adquirido_txt')),
                ('material_apoio', models.CharField(max_length=100, verbose_name=b'Material Apoio', db_column=b'material_apoio_txt')),
                ('gestor_estagiario', models.CharField(max_length=20, verbose_name=b'Gestor Estagiario', db_column=b'gestor_estagiario_txt')),
                ('tutor_estagiario', models.CharField(max_length=200, verbose_name=b'Tutor Estagiario', db_column=b'tutor_estagiario_txt')),
                ('comentario_tutor', models.CharField(max_length=200, verbose_name=b'Comentarios Tutor', db_column=b'comentario_tutor_txt')),
                ('comentario_estagiario', models.CharField(max_length=200, verbose_name=b'Comentarios Estagiario', db_column=b'comentario_estagiario_txt')),
                ('data_inicio', models.DateTimeField(verbose_name=b'Data Inicio')),
                ('data_fim', models.DateTimeField(verbose_name=b'Data Fim')),
            ],
            options={
                'db_table': 'acompanhamento_estagiario_atividade',
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PerfilEstagiario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'perfil_estagiario_id')),
                ('nome', models.CharField(max_length=50, verbose_name=b'Nome', db_column=b'nome_txt')),
                ('data_nascimento', models.DateTimeField(verbose_name=b'Data Nascimento')),
                ('instituicao_ensino', models.CharField(max_length=50, verbose_name=b'Instituicao de Ensino', db_column=b'instituicao_ensino_txt')),
                ('curso', models.CharField(max_length=50, verbose_name=b'Curso', db_column=b'curso_txt')),
                ('periodo_curso', models.IntegerField(verbose_name=b'Periodo Curso', db_column=b'periodo_txt')),
                ('previsao_formatura', models.DateTimeField(verbose_name=b'Previsao Formatura')),
                ('curso_extra', models.CharField(max_length=900, verbose_name=b'Cursos Extras', db_column=b'curso_extra_txt')),
                ('curso_rh', models.CharField(max_length=900, verbose_name=b'Cursos RH', db_column=b'curso_rh_txt')),
            ],
            options={
                'db_table': 'acompanhamento_estagiario_perfil_estagiario',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'tarefa_id')),
                ('descricao_tarefa', models.CharField(max_length=200, verbose_name=b'Descricao Tarefa', db_column=b'descricao_tarefa_txt')),
                ('principais_dificuldades', models.CharField(max_length=100, verbose_name=b'Principais Dificuldades', db_column=b'principais_dificuldades_txt')),
                ('status', models.CharField(max_length=15, verbose_name=b'Status', db_column=b'status_txt', choices=[(b'Concluida', b'Concluida'), (b'Em Andamento', b'Em Andamento'), (b'Parada', b'Parada')])),
                ('id_atividade', models.ForeignKey(to='projeto_estagiario.Atividade')),
            ],
            options={
                'db_table': 'acompanhamento_estagiario_tarefa',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, db_column=b'usuario_id')),
                ('email', models.CharField(max_length=30, verbose_name=b'Email', db_column=b'email_txt')),
                ('tipo_usuario', models.CharField(max_length=1, verbose_name=b'Tipo Usuario', db_column=b'tipo_usuario_txt')),
                ('senha', models.CharField(max_length=20, verbose_name=b'Senha', db_column=b'senha_txt')),
            ],
            options={
                'db_table': 'acompanhamento_estagiario_usuario',
            },
            bases=(models.Model,),
        ),
    ]
