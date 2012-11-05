from django.conf import settings
import sys
from socialaccess import app_settings


for _var in dir(app_settings):
    setattr(settings, _var, getattr(app_settings, _var))