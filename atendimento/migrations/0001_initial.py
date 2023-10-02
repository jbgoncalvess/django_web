# Generated by Django 4.2.5 on 2023-10-02 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionario', '0002_rename_endereco_funcionario_funcao'),
        ('cliente', '0001_initial'),
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField(help_text='Data e hora do atendimento', verbose_name='Horário')),
                ('situacao', models.CharField(choices=[('A', 'Agendado'), ('R', 'Realizado'), ('C', 'Cancelado')], default='A', help_text='Situação do atendimento', max_length=15, verbose_name='Situação')),
                ('cliente', models.ForeignKey(help_text='Nome do cliente', on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Cliente')),
                ('funcionario', models.ForeignKey(help_text='Nome do funcionário', on_delete=django.db.models.deletion.CASCADE, to='funcionario.funcionario', verbose_name='Funcionário')),
                ('servico', models.ForeignKey(help_text='Nome do serviço', on_delete=django.db.models.deletion.CASCADE, to='servico.servico', verbose_name='Serviço')),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
            },
        ),
    ]
