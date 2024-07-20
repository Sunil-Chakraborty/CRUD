"""
WSGI config for crudexample project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the sys.path
sys.path.append('/home/sunilc/CRUD')
sys.path.append('/home/sunilc/CRUD/crudexample')

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'crudexample.settings'

# Activate the virtual environment
activate_env = os.path.expanduser("/home/sunilc/CRUD/myenv/bin/activate_this.py")
with open(activate_env) as f:
    exec(f.read(), {'__file__': activate_env})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
