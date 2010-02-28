from organizadores.products.models import Category, Product, ProductAdmin, ProductHighlight, ProductHighlightAdmin
from django.contrib import admin

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductHighlight, ProductHighlightAdmin)
