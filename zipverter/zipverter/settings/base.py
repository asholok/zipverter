"""
Django settings for zipverter project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import logging    
import logging.handlers    
from django.conf import settings    

PATH_TO_SETTINGS = os.path.dirname(os.path.abspath(__file__)).split('/')
# VAR_ROOT = '/'.join(PATH_TO_SETTINGS[:-4])
BASE_DIR = '/'.join(PATH_TO_SETTINGS[:-2])



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2kp1c)9_94gu0)s+^%7-qoumivi^xnrs8q^ydfyn8*12tjclsq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'import_export',
    'cities',
    'tastypie',
    'handler',
    # 'debug_toolbar',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'zipverter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'zipverter.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'djgeo',
        'USER': os.getenv('DATABASE_USER', ''),
        'PASSWORD': os.getenv('DATABASE_PASS', ''),
        'HOST': os.getenv('DATABASE_HOST', ''),
        'PORT': '5432',
    }
}

CITIES_POSTAL_CODES = ['ALL']
CITIES_LOCALES = ['ALL']

CITIES_PLUGINS = [
    # Canada postal codes need region codes remapped to match geonames
    'cities.plugin.postal_code_ca.Plugin',  
]

# Internationalization 172.30.0.235
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
        # 'log_file':{
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': os.path.join(BASE_DIR, 'logs/django.log'),
        #     'maxBytes': '16777216',
        #     'formatter': 'verbose'
        # },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        'cities': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'handler': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },

        }
}
# INSTALLED_APPS += ("djsupervisor",)

logging.basicConfig()

