import oauth2 as oauth
import urllib, urllib2
import json

from django.conf import settings
from django.contrib.auth import authenticate

from socialaccess.clients import OAuth2Client



class OAuthGoogle(OAuth2Client):
    def __init__(self, callback_uri='socialaccess/googlecallback'):
        try:
            app_key = getattr(settings, 'GOOGLE_KEY')
            app_secret = getattr(settings, 'GOOGLE_SECRET')
            app_request_code_url = getattr(settings, 'GOOGLE_REQUEST_CODE_URL')
            app_access_token_url = getattr(settings, 'GOOGLE_ACCESS_TOKEN_URL')
        except AttributeError:
            raise Exception('One of these parameters is missing in settings.py: '\
                            'GOOGLE_KEY / GOOGLE_SECRET / GOOGLE_REQUEST_CODE_URL / GOOGLE_ACCESS_TOKEN_URL')
        OAuth2Client.__init__(self, callback_uri)
        self.client  = oauth.Client(oauth.Consumer(app_key, app_secret))
        self.request_code_url = app_request_code_url
        self.access_token_url = app_access_token_url
    

    def get_authorize_url(self, scope='https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile'):
        extra = '&response_type=code&state=/profile&access_type=online&approval_prompt=force'
        return super(OAuthGoogle, self).get_authorize_url(scope, extra)


    def get_access_token(self, oauth_verifier):
        extra = {'grant_type' : 'authorization_code',}
        return super(OAuthGoogle, self).get_access_token(oauth_verifier, extra)
    

    def get_profile_info(self, access_token):
        token = json.loads(unicode(access_token))
        url = getattr(settings, 'GOOGLE_PROFILE_URL', '')
        url = u'%s?access_token=%s' % (url, token['access_token'])        
        try:
            request = urllib2.Request(url=url)
            response = urllib2.urlopen(request)
        except IOError, e:
            raise e
        resp, content =  response.code, response.read()
        if resp != 200:
            raise Exception("Invalid response %s." % resp)        
        return json.loads(unicode(content))


    def authenticate(self, google_id):
        return authenticate(google_id=google_id)
