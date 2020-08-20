from .settings import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')