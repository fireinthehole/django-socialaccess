from django.conf import settings
from django.template import Library, Node
from django.template.loader import render_to_string

PROVIDER_CONNECT_INFO = {
    'facebook': {
        'connect_uri': 'fb_connect',
        'connect_button_img': 'FACEBOOK_CONNECT_IMAGE',
        'connect_button_cls': 'FACEBOOK_CONNECT_CLASS',
    },
    'linkedin': {
        'connect_uri': 'linkedin_connect',
        'connect_button_img': 'LINKEDIN_CONNECT_IMAGE',
        'connect_button_cls': 'LINKEDIN_CONNECT_CLASS',
    },
    'twitter': {
        'connect_uri': 'twitter_connect',
        'connect_button_img': 'TWITTER_CONNECT_IMAGE',
        'connect_button_cls': 'TWITTER_CONNECT_CLASS',
    },
    'google': {
        'connect_uri': 'google_connect',
        'connect_button_img': 'GOOGLE_CONNECT_IMAGE',
        'connect_button_cls': 'GOOGLE_CONNECT_CLASS',
    },
    'github': {
        'connect_uri': 'github_connect',
        'connect_button_img': 'GITHUB_CONNECT_IMAGE',
        'connect_button_cls': 'GITHUB_CONNECT_CLASS',
    },
}

register = Library()

class ConnectButton(Node):
    def __init__(self, site_name):
        self.site_name = site_name
    
    def render(self, context):
        params = {
            'provider': self.site_name,
            'btn_image_uri': getattr(settings, PROVIDER_CONNECT_INFO[self.site_name]['connect_button_img'], None),
            'btn_class': getattr(settings, PROVIDER_CONNECT_INFO[self.site_name]['connect_button_cls'], None),
            'provider_connect_uri': PROVIDER_CONNECT_INFO[self.site_name]['connect_uri'],
        }
        return render_to_string('socialaccess/connect_button.html', params)

 
def get_connect_button(parser, token):
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, "connect_button tag takes exactly 3 arguments"
    return ConnectButton(bits[1])
