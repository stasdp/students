
"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf import global_settings


import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!y3g^z5g98ezm1h=_5e5r+9$u437oy1gxrdfq=fx-bx_2r*8b8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# MODELS_DIRS = (
#     '/home/stas/dev/studentsdb/students/models',
# )

# TEMPLATE_DIRS = (
#     '/home/stas/dev/studentsdb/students/templates',
# )

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'students',
    'django_mandrill',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST' : 'localhost',
        'USER' : 'students_db_user',
        'PASSWORD' : '121212',
        'NAME' : 'students_db',
    }
}

        # 'NAME': os.path.join(BASE_DIR, '..', 'students_db.sqlite3'),
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'RU-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ADMIN_EMAIL = 'staspanuta@gmail.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'staspanuta@gmail.com'
EMAIL_HOST_PASSWORD = 'jZPP1HAaJOIp1N0Tsl5hPw'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'staspanuta@gmail.com'
EMAIL_BACKEND = 'django_mandrill.mail.backends.mandrillbackend.EmailBackend'
MANDRILL_API_KEY = "jZPP1HAaJOIp1N0Tsl5hPw" 


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

PORTAL_URL = 'http://localhost:8000'

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')

TEMPLATE_CONTEXT_PROCESSORS = \
    global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
    "studentsdb.context_processors.students_proc",
)
