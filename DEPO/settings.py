"""
Django settings for DEPO project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-k4vwk_hrj@2w9$p@cq*h=lex1i!=87opj0gzkyu#p$yg4hj-x7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#true local
#false Azure testing
#ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1',
                        'https://depocdev.azurewebsites.net', 'https://depocdev-staging.azurewebsites.net']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    "crispy_bootstrap4",
    'simple_history',
    'Agencias',
    #'Hallazgos',
    'Landing',
    'Usuarios',
    'Casos',
    'Compras',
    'CompraSometida',
    'django_tables2',
    'Multas',
    'storages',

]

if DEBUG:

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.security.SecurityMiddleware',
    ]
else:

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.cache.UpdateCacheMiddleware',

    ]

if 'DJANGO_DB_PASSWORD' in os.environ.keys():
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_table',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

ROOT_URLCONF = 'DEPO.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'DEPO.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DJANGO_DB_NAME'),
            'USER': os.environ.get('DJANGO_DB_USER'),
            'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
            'HOST': os.environ.get('DJANGO_DB_HOST'),
            'PORT': os.environ.get('DJANGO_DB_PORT'),
            'OPTIONS': {'sslmode': 'require', },
        }
    }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTHENTICATION_BACKENDS = [

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',

]



# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#STATIC_URL = '/static/'
#DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(CORE_DIR, 'static')
]



MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

AUTH_USER_MODEL = 'Usuarios.Usuario'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = "bootstrap4"

DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

###################AZURE#####################################

DEFAULT_FILE_STORAGE = 'DEPO.az_config.AzureMediaStorage'
STATICFILES_STORAGE = 'DEPO.az_config.AzureStaticStorage'

AZURE_STORAGE_KEY = os.environ.get('AZURE_STORAGE_KEY', False)
AZURE_ACCOUNT_NAME = "depodevstorage"
AZURE_MEDIA_CONTAINER = os.environ.get('AZURE_MEDIA_CONTAINER', 'media')
AZURE_STATIC_CONTAINER = os.environ.get('AZURE_STATIC_CONTAINER', 'static')

AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.azureedge.net'  # CDN URL


if DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"