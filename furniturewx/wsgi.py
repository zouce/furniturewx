"""
WSGI config for furniturewx project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/home/zouce/furniture')
sys.path.append('/home/zouce/anaconda3/envs/furniture/lib/python3.9/site-packages/django/bin')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'furniturewx.settings')

application = get_wsgi_application()
