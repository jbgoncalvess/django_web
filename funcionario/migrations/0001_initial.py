# Generated by Django 4.2.5 on 2023-10-02 13:04

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo', max_length=50, verbose_name='Nome')),
                ('fone', models.CharField(help_text='Número do telefone', max_length=15, verbose_name='Telefone')),
                ('email', models.EmailField(help_text='Endereço de E-mail', max_length=100, unique=True, verbose_name='E-mail')),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='pessoas', variations={'thumbnail': {'crop': True, 'height': 100, 'width': 100}}, verbose_name='Foto')),
                ('endereco', models.CharField(help_text='Função na empresa', max_length=35, verbose_name='Função')),
                ('data_admissao', models.DateTimeField(help_text='Data de admissão na empresa', verbose_name='Admissão')),
            ],
            options={
                'verbose_name': 'Funcionário',
                'verbose_name_plural': 'Funcionários',
            },
        ),
    ]
