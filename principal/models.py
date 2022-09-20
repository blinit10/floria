from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils.safestring import mark_safe


class AntecedentesInformatica(models.Model):
    texto = RichTextField()

    def __str__(self):
        if len(mark_safe(self.texto)) > 50:
            return 'Antecedentes de la informatica'
        return 'Antecedentes de la informatica'

    class Meta:
        verbose_name = 'Antecedentes de la Informática'
        verbose_name_plural = 'Antecedentes de la Informática'
        app_label = 'sistema'

class PersonalidadDestacada(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    fecha_muerte = models.DateField()
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='personalidades/')

    def __str__(self):
        return self.nombre

    def miniatura(self):
        return mark_safe('<img src="'+ self.foto.url +'" width="120">')
    miniatura.short_description = 'Vista previa'
    miniatura.allow_tags =True

    class Meta:
        verbose_name = 'Personalidad Destacada'
        verbose_name_plural = 'Personalidades Destacadas'

class Generacion(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return str(self.fecha_inicio) + ' - ' + str(self.fecha_fin)

    class Meta:
        verbose_name = 'Generación'
        verbose_name_plural = 'Generaciones'

class Maquina(models.Model):
    generacion = models.ForeignKey(Generacion, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    fecha_creacion = models.DateField()
    descripcion = RichTextField()
    foto = models.ImageField(upload_to='maquinas/')

    def __str__(self):
        return self.nombre

    def miniatura(self):
        return mark_safe('<img src="'+ self.foto.url +'" width="120">')
    miniatura.short_description = 'Vista previa'
    miniatura.allow_tags =True

    class Meta:
        verbose_name = 'Máquina'
        verbose_name_plural = 'Máquinas'

class InformaticaCuba(models.Model):
    texto = RichTextField()

    def __str__(self):
        return 'La infromática en Cuba'

    class Meta:
        verbose_name = 'La Informática en Cuba'
        verbose_name_plural = 'La Informática en Cuba'
        app_label = 'sistema'

class Banner(models.Model):
    autor = models.CharField(max_length=255, verbose_name='Autor')
    frase = models.TextField(verbose_name='Frase')
    imagen = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.frase

    class Meta:
        verbose_name = 'Cintillo con frase'
        verbose_name_plural = 'Cintillo con frase'
        app_label = 'sistema'

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255)

    def __str__(self):
        return self.pregunta

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
        app_label = 'trivia'

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.CharField(max_length=255)
    correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.respuesta

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        app_label = 'trivia'

class Jugador(models.Model):
    nombre = models.CharField(max_length=255)
    puntuacion = models.IntegerField(default=0)
    hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        app_label = 'trivia'

class Nodo(models.Model):
    fecha = models.DateField()
    evento = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to='nodos/', null=True, blank=True, help_text='Opcional')

    def __str__(self):
        return '{}'.format(self.evento)

    class Meta:
        verbose_name = 'Nodo de línea temporal'
        verbose_name_plural = 'Nodos de línea temporal'
        app_label = 'sistema'

class LugarInteres(models.Model):
    nombre = models.CharField(max_length=255)
    img_principal = models.ImageField(upload_to='tours/')
    direccion = models.TextField()
    descripcion = models.TextField(verbose_name='Descripción')
    tour = models.TextField(help_text='Pega aquí el código embebido de https://momento360.com/')
    visible = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name = 'Lugar de interés'
        verbose_name_plural = 'Lugares de interés'
        app_label = 'principal'




