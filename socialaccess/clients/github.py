import oauth2 as oauth
import urllib
import json

from django.conf import settings
from django.contrib.auth import authenticate

from socialaccess.clients import OAuth2Client



class OAuthGithub(OAuth2Client):
    def __init__(self, callback_uri='socialaccess/fbcallback'):
        OAuth2Client.__init__(self, callback_uri)
        self.client  = oauth.Client(oauth.Consumer(
                                                    getattr(settings, 'GITHUB_KEY', ''),
                                                    getattr(settings, 'GITHUB_SECRET', '')))
        self.request_code_url = getattr(settings, 'GITHUB_REQUEST_CODE_URL', '')
        self.access_token_url = getattr(settings, 'GITHUB_ACCESS_TOKEN_URL', '')
    

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
