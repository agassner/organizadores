from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # Admin    
    (r'^admin/', include(admin.site.urls)),

    # JSON response for the products
    (r'^products/', include('organizadores.products.urls')),

    # Media config
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Front end urls
    (r'^contato/?$', 'organizadores.views.contact'),
    (r'^contato/enviar?$', 'organizadores.views.contact_send'),
    (r'^produtos/?$', 'organizadores.views.products'),
    (r'^preview/?$', 'organizadores.views.preview'),
    (r'^$', 'organizadores.views.index'),
)
