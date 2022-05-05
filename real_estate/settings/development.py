from .base import *

DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE'),
        'NAME': env('POSTGRES_NAME'),
        'USER':  env('POSTGRES_USER'),
        'PASSWORD':env('POSTGRES_PASSWORD'),
        'HOST':env('POSTGRES_HOST'),
        'PORT':env('POSTGRES_PORT'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
DEFAULT_FROM_EMAIL = "info@real-estate.com"
DOMAIN = env("DOMAIN")
SITE_NAME = "Real Estate"