from django.contrib import admin
from .models import *

#inlines
class MaquinaInline(admin.StackedInline):
    model = Maquina
    extra = 0
    fieldsets = (
        ('', {
            'fields': ('nombre', 'fecha_creacion', 'descripcion',)
        }),
        ('', {
            'fields': (('foto', 'miniatura'),)
        }),
    )
    readonly_fields = ['miniatura',]

class RespuestaInline(admin.StackedInline):
    model = Respuesta
    extra = 0
    fieldsets = (
        ('', {
            'fields': ('respuesta', 'correcta',)
        }),
    )
    max_num = 4
    min_num = 1

#model admins
class GeneracionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
    list_per_page = 10
    search_fields = ['nombre', ]
    list_display_links = ('nombre', 'fecha_inicio', 'fecha_fin')
    list_filter = ['fecha_inicio', 'fecha_fin']
    fieldsets = (
        ('', {
            'fields': ('nombre', 'fecha_inicio', 'fecha_fin')
        }),
    )
    inlines = [MaquinaInline, ]

class PersonalidadDestacadaAdmin(admin.ModelAdmin):
    list_display = ('miniatura','nombre', 'fecha_nacimiento', 'fecha_muerte')
    list_per_page = 5
    search_fields = ['nombre', 'descripcion']
    list_display_links = ('miniatura','nombre', 'fecha_nacimiento', 'fecha_muerte')
    list_filter = ['fecha_nacimiento', 'fecha_muerte']
    fieldsets = (
        ('Datos principales', {
            'fields': ('nombre', 'fecha_nacimiento', 'fecha_muerte')
        }),
        ('Historia', {
            'fields': ('descripcion', )
        }),('Multimedia', {
            'fields': ('foto', 'miniatura')
        }),
    )
    readonly_fields = ['miniatura', ]

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta',)
    list_per_page = 10
    search_fields = ['pregunta', ]
    list_display_links = ('pregunta',)
    fieldsets = (
        ('', {
            'fields': ('pregunta',)
        }),
    )
    inlines = [RespuestaInline, ]

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('puntuacion','nombre', 'hora',)
    list_per_page = 5
    search_fields = ['nombre', ]
    list_display_links = ('puntuacion','nombre', 'hora',)
    list_filter = ['puntuacion', 'hora']
    fieldsets = (
        ('Datos principales', {
            'fields': ('nombre', 'puntuacion')
        }),
    )

class NodoAdmin(admin.ModelAdmin):
    list_display = ['fecha', 'evento']
    list_display_links = ['fecha', 'evento']


# Register your models here.
admin.site.register(AntecedentesInformatica)
admin.site.register(PersonalidadDestacada, PersonalidadDestacadaAdmin)
admin.site.register(Generacion, GeneracionAdmin)
admin.site.register(InformaticaCuba)
admin.site.register(Banner)
admin.site.register(Nodo, NodoAdmin)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Jugador, JugadorAdmin)

