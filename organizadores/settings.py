# -*- coding: utf-8 -*-

# Django settings for organizadores project.

from os.path import join, dirname, abspath

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Administrador', 'administrador@organizadores.com.br'),
)

LOCAL_FILE = lambda *x: abspath(join(dirname(__file__), *x))

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'       # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'organizadores' # Or path to database file if using sqlite3.
DATABASE_USER = 'organizadores' # Not used with sqlite3.
DATABASE_PASSWORD = '8e3Egsp'   # Not used with sqlite3.
DATABASE_HOST = ''              # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''              # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = LOCAL_FILE('media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'fuh1z-73%zy*^bu_k*s=grby3ql(_!b&)6p4l1io9q+c9$dutn'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'organizadores.urls'

TEMPLATE_DIRS = (
    LOCAL_FILE('templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'organizadores.products',
)

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'organizadores'
EMAIL_HOST_PASSWORD = 'b35f473a'
DEFAULT_FROM_EMAIL = 'administrador@organizadores.com.br'
SERVER_EMAIL = 'organizadores@organizadores.com.br'

