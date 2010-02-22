from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'organizadores.products.views.list_products'),
    (r'^(?P<product_id>\d+)/$', 'organizadores.products.views.get_product'),

    (r'^categories/$', 'organizadores.products.views.list_categories'),

    (r'^highlights/$', 'organizadores.products.views.list_highlights'),
    (r'^highlights/slide', 'organizadores.products.views.list_highlights_slide'),
    (r'^highlights/box', 'organizadores.products.views.list_highlights_box'),
    (r'^highlights/top', 'organizadores.products.views.list_highlights_top'),
    (r'^highlight/(?P<highlight_id>\d+)/$', 'organizadores.products.views.get_highlight'),
)
