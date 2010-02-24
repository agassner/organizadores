import os, sys
sys.path.append('/home/arthur/organizadores/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'organizadores.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
