# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Noticia, Categoria
from django.template import RequestContext, loader


def index(request):
	#data = {}
	#data['object_list'] = Noticia.objects.order_by('-created')[:6]
	object_list = Noticia.objects.order_by('-created')[:6]
	#data2 = {}
	#data['noticia_destacada'] = Noticia.objects.filter(is_destacada=True)[:1]
	noticia_destacada = Noticia.objects.filter(is_destacada=True).order_by('-created')[:1]
	template = 'noticias/index.html'
	return render(request, template, {'object_list':object_list, 'noticia_destacada':noticia_destacada})

    #ultima_noticia_list = Categoria.objects.order_by('created')[:5]
    #output = [p.name for p in ultima_noticia_list]
    #return HttpResponse(output)

def detalle_noticia(request, pk):
    template_name = 'noticias/noticia_detalle.html'
    noticia_detalle = Noticia.objects.get(pk=pk)

    return render(request, template_name, {'noticia_detalle':noticia_detalle})