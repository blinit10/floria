# Generated by Django 3.2.12 on 2022-06-05 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='antecedentesinformatica',
            options={'verbose_name': 'Antecedentes de la Informática', 'verbose_name_plural': 'Antecedentes de la Informática'},
        ),
        migrations.AlterModelOptions(
            name='generacion',
            options={'verbose_name': 'Generación', 'verbose_name_plural': 'Generaciones'},
        ),
        migrations.AlterModelOptions(
            name='informaticacuba',
            options={'verbose_name': 'La Informática en Cuba', 'verbose_name_plural': 'La Informática en Cuba'},
        ),
        migrations.AlterModelOptions(
            name='maquina',
            options={'verbose_name': 'Máquina', 'verbose_name_plural': 'Máquinas'},
        ),
        migrations.AlterModelOptions(
            name='personalidaddestacada',
            options={'verbose_name': 'Personalidad Destacada', 'verbose_name_plural': 'Personalidades Destacadas'},
        ),
        migrations.AddField(
            model_name='generacion',
            name='nombre',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]