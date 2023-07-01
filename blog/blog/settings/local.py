from .base import  *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&_t%**s4eca=m8+jxb!s23#&u9^%yy+%g!2^y0xlj2p3i4@v40'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
