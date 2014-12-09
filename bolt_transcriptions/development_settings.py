import os
from bolt_transcriptions.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
#LANGUAGE_CODE = 'ar-iq'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    "/Users/enoriega/BOLT/UnivAriz-2/P3Testing_UnivAriz-2",
    '/var/www/static/',
)
# Dataset files directory
DATASET_DIR = "%s/../dataset/" % BASE_DIR
