from django.db import models

class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=200)
    description = models.TextField()
    #image = models.ImageField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    
class ProductHighlight(models.Model):
    product = models.ForeignKey('Product')
    title = models.CharField(null=False, blank=False, max_length=200)
    subtitle = models.CharField(null=False, blank=True, max_length=200)
    content = models.TextField()
    #link

    class Meta:
        verbose_name = "Produto em destaque"
        verbose_name_plural = "Produtos em destaque"
