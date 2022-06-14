# Generated by Django 3.2.3 on 2022-06-14 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20220605_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=255, verbose_name='Título')),
                ('frase', models.TextField(verbose_name='Subtítulo')),
                ('imagen', models.ImageField(upload_to='banner/')),
            ],
            options={
                'verbose_name': 'Cintillo con frase',
                'verbose_name_plural': 'Cintillo con frase',
            },
        ),
    ]
