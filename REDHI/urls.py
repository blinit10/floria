"""REDHI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from REDHI import settings
from principal.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = 'index'),
    path('antecedentes/', antecedentes_detalles, name = 'antecedentes_detalles '),
    path('informatica en cuba/', informatica_cuba_detalles, name = 'informatica_cuba_detalles '),
    path('juega y aprende/', juega_aprende, name = 'juega_aprende'),
    path('puntuaciones/', puntuaciones, name = 'puntuaciones'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Panel de Control'