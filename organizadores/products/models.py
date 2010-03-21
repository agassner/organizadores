# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, verbose_name="Nome")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['name']

class Product(models.Model):
    category = models.ForeignKey('Category', verbose_name="Categoria")
    name = models.CharField(null=False, blank=False, max_length=200, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    photo = models.ImageField(upload_to='uploaded', db_column='photo', blank=True, verbose_name="Foto")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'creation_date')

class ProductHighlight(models.Model):
    HIGHLIGHT_AREA_CHOICES = (
        (u'S', u'Slide'),
        (u'B', u'Box'),
        (u'T', u'Top'),
    )

    product = models.ForeignKey('Product', verbose_name="Produto")
    title = models.CharField(null=False, blank=False, max_length=200, verbose_name="Título")
    subtitle = models.CharField(null=False, blank=True, max_length=200, verbose_name="Sub-título")
    content = models.TextField(verbose_name="Conteúdo")
    photo = models.ImageField(upload_to='uploaded', db_column='photo', blank=True, verbose_name="Foto")
    area = models.CharField(max_length=2, choices=HIGHLIGHT_AREA_CHOICES, verbose_name="Área de Destaque")
    link = models.SlugField(max_length=200, verbose_name="Link")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Produto em destaque"
        verbose_name_plural = "Produtos em destaque"
        ordering = ['creation_date']

class ProductHighlightAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'area', 'creation_date')
    list_filter = ['area']

