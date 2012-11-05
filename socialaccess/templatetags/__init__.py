from django.conf import settings
from django.template import Library, Node
from django.template.loader import render_to_string
     
register = Library()
     
class ConnectButton(Node):
    def __init__(self, site_name):
        self.site_name = site_name
    
    def render(self, context):
        if self.site_name == 'facebook':
            template_name = 'facebook/connect_button.html'
            image_url = getattr(settings, 'FACEBOOK_CONNECT_IMAGE', '')
        elif self.site_name == 'linkedin':
            template_name = 'linkedin/connect_button.html'
            image_url = getattr(settings, 'LINKEDIN_CONNECT_IMAGE', '')
        elif self.site_name == 'twitter':
            template_name = 'twitter/connect_button.html'
            image_url = getattr(settings, 'TWITTER_CONNECT_IMAGE', '')
        elif self.site_name == 'google':
            template_name = 'google/connect_button.html'
            image_url = getattr(settings, 'GOOGLE_CONNECT_IMAGE', '')
        elif self.site_name == 'github':
            template_name = 'github/connect_button.html'
            image_url = getattr(settings, 'GITHUB_CONNECT_IMAGE', '')
        else:
            return ''
        return render_to_string(template_name, {'image_url' : image_url})
 
def get_connect_button(parser, token):
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, "connect_button tag takes exactly 3 arguments"
    return ConnectButton(bits[1])