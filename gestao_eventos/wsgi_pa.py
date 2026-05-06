"""
WSGI config for gestao_eventos project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
import sys

# Add your project path here
path = '/home/gestaoeventosmp'

if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gestao_eventos.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()