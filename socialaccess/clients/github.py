import json
import oauth2 as oauth

from django.conf import settings
from django.contrib.auth import authenticate

from socialaccess.clients import OAuth2Client


class OAuthGithub(OAuth2Client):
    def __init__(self, callback_uri='socialaccess/fbcallback'):
        OAuth2Client.__init__(self, callback_uri)
        try:
            app_key = getattr(settings, 'GITHUB_KEY')
            app_secret = getattr(settings, 'GITHUB_SECRET')
            app_request_code_url = getattr(settings, 'GITHUB_REQUEST_CODE_URL')
            app_access_token_url = getattr(settings, 'GITHUB_ACCESS_TOKEN_URL')
        except AttributeError:
            raise Exception('One of these parameters is missing in settings.py: '\
                            'GITHUB_KEY / GITHUB_SECRET / GITHUB_REQUEST_CODE_URL / GITHUB_ACCESS_TOKEN_URL')

        self.client  = oauth.Client(oauth.Consumer(app_key, app_secret))
        self.request_code_url = app_request_code_url
        self.access_token_url = app_access_token_url
    

    def get_authorize_url(self, scope='user,public_repo'):
        return super(OAuthGithub, self).get_authorize_url(scope=scope)
    

    def get_profile_info(self, access_token):
        url = getattr(settings, 'GITHUB_PROFILE_URL', '')
        url = u'%s?access_token=%s' % (url, access_token)

        resp, content = self.client.request(url)
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])        
        return json.loads(unicode(content))


    def authenticate(self, github_id):
        return authenticate(github_id=github_id)
