"""
WSGI config for django_init project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Enlaza el archvivo de settings con el archivo de configuración del proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_init.settings')

application = get_wsgi_application()
