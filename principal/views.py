import random
from typing import re

from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import *

# Create your views here.
def index(request):
    antecedentes = mark_safe(AntecedentesInformatica.objects.all()[0].texto)
    primero = PersonalidadDestacada.objects.first()
    ultimos = PersonalidadDestacada.objects.all().order_by('-id')
    generaciones = Generacion.objects.order_by('-fecha_inicio')
    banner = Banner.objects.all()[0]
    informatica_cuba = mark_safe(InformaticaCuba.objects.all()[0].texto)
    return render(request, 'principal/index.html',{'antecedentes':antecedentes, 'primero':primero,
                                                   'ultimos':ultimos, 'generaciones':generaciones,
                                                   'banner':banner,
                                                   'informatica_cuba':informatica_cuba})

def antecedentes_detalles(request):
    antecedentes = mark_safe(AntecedentesInformatica.objects.all()[0].texto)
    return render(request, 'principal/antecedentes_detail.html', {'antecedentes': antecedentes,'flag':True})

def informatica_cuba_detalles(request):
    informatica_cuba = mark_safe(InformaticaCuba.objects.all()[0].texto)
    return render(request, 'principal/informatica_cuba_detail.html', {'informatica_cuba': informatica_cuba,'flag':True})

def juega_aprende(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'principal/juega_aprende.html', {'preguntas': preguntas})

def puntuaciones(request):
    if request.method == 'POST':
        jugador = Jugador(nombre=request.POST['nombre'], puntuacion=int(request.POST['puntos']))
        jugador.save()
        # jugadores = {}
        # for player in Jugador.objects.order_by('-puntuacion'):
        #     jugadores[player.pk] = []
        #     jugadores[player.pk].append(player.nombre)
        #     jugadores[player.pk].append(player.puntuacion)
        #     jugadores[player.pk].append(player.hora)
        return JsonResponse(data={'satus':200}, safe=False)
    pares = {}
    for player in Jugador.objects.all():
        pares[player.pk] = []
        r = lambda: random.randint(0, 255)
        s = lambda: random.randint(0, 255)
        pares[player.pk].append('#%02X%02X%02X' % (r(), r(), r()))
        pares[player.pk].append('#%02X%02X%02X' % (s(), s(), s()))
    return render(request, 'principal/puntuaciones.html', {'jugadores':Jugador.objects.order_by('-puntuacion'),
                                                           'pares':pares})
