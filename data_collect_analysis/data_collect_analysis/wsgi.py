"""
WSGI config for data_collect_analysis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "data_collect_analysis.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
