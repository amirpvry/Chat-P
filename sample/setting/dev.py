from sample.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2a4&m@yy$=*-b@)q27-apsd^0tahw8zjg47b07b8)qqnn)(pz+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [ '127.0.0.1' , '127.0.0.1:8000' , ]

# 
# sites framework
SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics"
]

X_FRAME_OPTIONS = "SAMEORIGIN"

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
