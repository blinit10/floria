# Generated by Django 3.2.3 on 2022-06-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_pregunta_respuesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('puntuacion', models.IntegerField(default=0)),
                ('hora', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
            },
        ),
    ]
