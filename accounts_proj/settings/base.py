# -*- coding: utf-8 -*-

from unipath import Path


PROJECT_ROOT = Path(__file__).ancestor(3)

ADMINS = (
    ('Bernardo Brik', 'bernardobrik@gmail.com'),
)

MANAGERS = ADMINS


ALLOWED_HOSTS = []

TIME_ZONE = 'America/Sao_Paulo'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = PROJECT_ROOT.child('public').child('media')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_ROOT.child('public').child('static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_ROOT.child('static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ur1r9rbw=&728)disr1*#ewq5%gdp^5pt$l0b^5@s3l1^e9e69'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'accounts_proj.urls'

WSGI_APPLICATION = 'accounts_proj.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_ROOT.child('templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    # 'django.contrib.admin',
    # 'django.contrib.admindocs',
)


LOGIN_REDIRECT_URL = 'home:home'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'