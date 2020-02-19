"""
Django settings for chat_app project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_TO_HEROKU = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*t&hojtfetrz0xq)c=191u&p4f@60&p3)v)yak%as**et1vf6h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'friends',
    'notification',
    'chatmessages',
    'group',
    'error'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'chat_app.urls'

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

WSGI_APPLICATION = 'chat_app.wsgi.application'
ASGI_APPLICATION = "chat_app.routing.application"

if DEBUG:
    # for development
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
elif UPLOAD_TO_HEROKU:
    import dj_database_url

    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
else:
    # for production
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'chatapp',
            'HOST': '103.107.26.2',
            'PORT': '3306',
            'USER': 'root',
            'PASSWORD': 'Inexture@12#',
        }
    }

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [('localhost', '6379')],
        },
    },
}
ASGI_APPLICATION = 'chat_app.routing.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
if DEBUG:
    # for development
    STATIC_URL = '/static/'
else:
    # for production
    STATIC_URL = 'http://103.107.26.2/django_chat/chat_app/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'chat_app/static')
]

MEDIA_URL = '/media/' if DEBUG else 'http://103.107.26.2:8001/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

FILE_UPLOAD_PERMISSIONS = 0o640
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880

AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '../../login'
LOGIN_REDIRECT_URL = '../login'

LOGOUT_URL = '../../logout'
LOGOUT_REDIRECT_URL = '../login'

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = ''  # email id
EMAIL_HOST_PASSWORD = ''  # password
EMAIL_USE_TLS = True

django_heroku.settings(locals())
