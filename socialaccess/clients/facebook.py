import oauth2 as oauth
import urllib
import json

from django.conf import settings
from django.contrib.auth import authenticate

from socialaccess.clients import OAuth2Client



class OAuthFacebook(OAuth2Client):
    def __init__(self, callback_uri='socialaccess/fbcallback'):
        try:
            app_key = getattr(settings, 'FACEBOOK_KEY')
            app_secret = getattr(settings, 'FACEBOOK_SECRET')
            app_request_code_url = getattr(settings, 'FACEBOOK_REQUEST_CODE_URL')
            app_access_token_url = getattr(settings, 'FACEBOOK_ACCESS_TOKEN_URL')
        except AttributeError:
            raise Exception('One of these parameters is missing in settings.py: '\
                            'FACEBOOK_KEY / FACEBOOK_SECRET / FACEBOOK_REQUEST_CODE_URL / FACEBOOK_ACCESS_TOKEN_URL')
        OAuth2Client.__init__(self, callback_uri)
        self.client  = oauth.Client(oauth.Consumer(app_key, app_secret))
        self.request_code_url = app_request_code_url
        self.access_token_url = app_access_token_url
    

    def get_authorize_url(self, scope='email, read_stream,user_photos,user_videos'):
        return super(OAuthFacebook, self).get_authorize_url(scope=scope)
    

    def get_profile_info(self, access_token):
        url = getattr(settings, 'FACEBOOK_PROFILE_URL', 'https://graph.facebook.com')
        url = u'%s/me?%s' % (url, access_token)

        resp, content = self.client.request(url)
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])        
        return json.loads(unicode(content))


    def authenticate(self, fb_id):
        return authenticate(fb_id=fb_id)
