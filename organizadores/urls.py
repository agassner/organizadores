from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^products/', include('organizadores.products.urls')),

    (r'^admin/', include(admin.site.urls)),
)
