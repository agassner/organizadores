# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('base.html')

def contact(request):
    return render_to_response('contato.html')

def products(request):
    return render_to_response('produtos.html')

def preview(request):
    return render_to_response('preview.html')
