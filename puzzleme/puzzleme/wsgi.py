"""
WSGI config for puzzleme project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

sys.path.append('C:/dev/django_projects/puzzleme')
sys.path.append('C:/dev/django_projects/puzzleme/puzzleme')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puzzleme.settings')
# os.environ["DJANGO_SETTINGS_MODULE"] = "puzzleme.settings"
application = Cling(get_wsgi_application())
