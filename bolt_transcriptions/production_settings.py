import os
from bolt_transcriptions.settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', 'b4.sista.arizona.edu']


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    },

    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'bolt_transcriptions',
        'USER': 'enoriega',
        'PASSWORD': 'w7PxNoAojIWsDA',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Dataset files directory
#DATASET_DIR = "%s/../dataset/" % BASE_DIR

STATICFILES_DIRS = (
    "/home/enoriega/UnivAriz-2/P3Testing_UnivAriz-2/",
)
