# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Nome")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']

class Product(models.Model):
    category = models.ForeignKey('Category')
    name = models.CharField(null=False, blank=False, max_length=200, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    #image = models.ImageField()
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
class ProductHighlight(models.Model):
    HIGHLIGHT_AREA_CHOICES = (
        (u'S', u'Slide'),
        (u'B', u'Box'),
        (u'T', u'Top'),
    )

    product = models.ForeignKey('Product')
    title = models.CharField(null=False, blank=False, max_length=200, verbose_name="Título")
    subtitle = models.CharField(null=False, blank=True, max_length=200, verbose_name="Sub-título")
    content = models.TextField(verbose_name="Conteúdo")
    area = models.CharField(max_length=2, choices=HIGHLIGHT_AREA_CHOICES, verbose_name="Área de Destaque")
    #link

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Produto em destaque"
        verbose_name_plural = "Produtos em destaque"
