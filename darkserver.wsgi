#!/usr/bin/python
import os
import sys

sys.path.append('/etc/darkserver/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

