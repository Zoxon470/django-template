from datetime import timedelta
from typing import Tuple

import environ
from django.utils.translation import gettext_lazy as _

from server.settings.components import BASE_DIR

# Environment variables library for django
# https://github.com/joke2k/django-environ

env = environ.Env()

SECRET_KEY = env.str('DJANGO_SECRET_KEY')

# Application definition:

INSTALLED_APPS: Tuple[str, ...] = (
    # Your apps here:
    'server.apps.common',

    # Default django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-admin:
    'django.contrib.admin',
    'django.contrib.admindocs',

    # DRF
    'rest_framework',

    # Security:

    # Health checks:
    # You may want to enable other checks as well,
    # see: https://github.com/KristianOellegaard/django-health-check
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',
    'health_check.contrib.redis',
)

MIDDLEWARE: Tuple[str, ...] = (
    # Logging:
    'server.settings.components.logging.LoggingContextVarsMiddleware',

    # Django:
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'server.settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'server.settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': env.db_url('DATABASE_URL')
}
DATABASES['default']['CONN_MAX_AGE'] = env.int(
    'CONN_MAX_AGE', default=60
)
DATABASES['default']['OPTIONS'] = {
    'connect_timeout': 10,
    'options': '-c statement_timeout=15000ms',
}

DATETIME_FORMAT = '%d/%m/%Y %H:%M:%S'
DATETIME_INPUT_FORMATS = [DATETIME_FORMAT]
DATE_FORMAT = '%d/%m/%Y'
DATE_INPUT_FORMATS = [DATE_FORMAT]
TIME_FORMAT = '%H:%M:%S'
TIME_INPUT_FORMATS = [TIME_FORMAT]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DATETIME_FORMAT': '%d/%m/%Y %H:%M:%S',
    'DATETIME_INPUT_FORMATS': ['%d/%m/%Y %H:%M:%S'],
    'DATE_FORMAT': '%d/%m/%Y',
    'DATE_INPUT_FORMATS': ['%d/%m/%Y'],
    'TIME_FORMAT': '%H:%M:%S',
    'TIME_INPUT_FORMATS': ['%H:%M:%S'],
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(
        minutes=env.int('JWT_ACCESS_TOKEN_LIFETIME', 5)
    )
}

SPECTACULAR_SETTINGS = {
    'TITLE': '{{cookiecutter.project_name}}',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)

LOCALE_PATHS = (
    'locale/',
)

USE_TZ = True
TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATICFILES_DIRS = [BASE_DIR.joinpath('server/static')]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Media files
# Media root dir is commonly changed in production
# (see development.py and production.py).
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

# Django authentication system
# https://docs.djangoproject.com/en/4.2/topics/auth/

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Security
# https://docs.djangoproject.com/en/4.2/topics/security/



# Email configuration
# https://docs.djangoproject.com/en/4.2/ref/settings/#email-backend

EMAIL_USER_SENDER = env.str('EMAIL_USER_SENDER')
EMAIL_CONFIG = env.email_url('EMAIL_URL')
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 5

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
