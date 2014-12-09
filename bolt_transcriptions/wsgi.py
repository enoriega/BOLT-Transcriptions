"""
WSGI config for bolt_transcriptions project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/home/enoriega/.virtualenvs/BOLT-Transcriptions/lib/python2.7/site-packages')
sys.path.append('/var/www/bolt-transcriptions')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bolt_transcriptions.production_settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
