# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import PostForm
from .models import Post

from django.http import HttpResponse
import json

def inicio(request):

	dic = {

		'post':Post.objects.reverse(),
		'form':PostForm

	}

	return render(request, 'inicio.html', dic)

def crear_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('el_post')
        response_data = {}

        post = Post(texto=post_text, autor=request.user)
        post.save()

        response_data['result'] = 'Post creado exitosamente!'
        response_data['postpk'] = post.pk
        response_data['texto'] = post.texto
        response_data['creado'] = post.creado.strftime('%B %d, %Y %I:%M %p')
        response_data['autor'] = post.autor.username

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nada para ver": "esto no ocurrio"}),
            content_type="application/json"
        )