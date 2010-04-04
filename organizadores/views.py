# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from organizadores.products.models import Product

def index(request):
    return render_to_response('base.html')

def contact(request):
    return render_to_response('contato.html')

def contact_send(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    message = request.POST.get('message', '')

    if name and email and message:
        try:
            send_mail("Organizadores.com.br - Contato", message, email, ['contato@organizadores.com.br'])
        except BadHeaderError:
            return HttpResponse('{"result": "fail", "message": "Invalid header found."}', mimetype="application/json")

        return HttpResponse('{"result": "success", "message": "Muito obrigado pelo contato. Em breve retornaremos a sua mensagem."}', mimetype="application/json")
    else:
        return HttpResponse('{"result": "fail", "message": "Favor preencher todos os campos para o envio do contato."}', mimetype="application/json")

def products(request):
    products_list = Product.objects.all()
    return render_to_response('produtos.html', {'products_list': products_list})

def about(request):
    return render_to_response('sobre.html')

def preview(request):
    return render_to_response('preview.html')
