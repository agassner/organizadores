# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core import serializers
from organizadores.products.models import Category, Product, ProductHighlight

def list_products(request):
    data = serializers.serialize("json", Product.objects.all(), fields=("name", "description", "price", "creation_date"), ensure_ascii=False)
    return HttpResponse(data)

def get_product(request, product_id):
    data = serializers.serialize("json", Product.objects.filter(pk=product_id), fields=("name", "description", "price", "creation_date"), ensure_ascii=False)
    return HttpResponse(data)

def list_categories(request):
    data = serializers.serialize("json", Category.objects.all(), ensure_ascii=False)
    return HttpResponse(data)

def list_highlights(request):
    data = serializers.serialize("json", ProductHighlight.objects.all(), ensure_ascii=False)
    return HttpResponse(data)

def get_highlight(request, highlight_id):
    data = serializers.serialize("json", ProductHighlight.objects.filter(pk=highlight_id), ensure_ascii=False)
    return HttpResponse(data)
