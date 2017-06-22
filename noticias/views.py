# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Noticia, Categoria
from django.template import RequestContext, loader


def index(request):
	data = {}
	data['object_list'] = Noticia.objects.order_by('-created')
	template = 'noticias/index.html'
	return render(request, template, data)

    #ultima_noticia_list = Categoria.objects.order_by('created')[:5]
    #output = [p.name for p in ultima_noticia_list]
    #return HttpResponse(output)