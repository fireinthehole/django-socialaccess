from django.template import Library
from socialaccess.templatetags import get_connect_button

register = Library()

register.tag('connect_button', get_connect_button)