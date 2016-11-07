import json
import oauth2 as oauth
import urllib.request
from urllib.parse import urlencode
from django.conf import settings
from django.contrib.auth import authenticate
from socialaccess.clients import OAuth2Client


class OAuthLinkedIn(OAuth2Client):
    def __init__(self, callback_uri='socialaccess/linkedincallback'):
        app_key = getattr(settings, 'LINKEDIN_KEY')
        app_secret = getattr(settings, 'LINKEDIN_SECRET')
        app_request_code_url = getattr(settings, 'LINKEDIN_REQUEST_CODE_URL')
        app_access_token_url  = getattr(settings, 'LINKEDIN_ACCESS_TOKEN_URL')

        OAuth2Client.__init__(self, callback_uri)
        self.client  = oauth.Client(oauth.Consumer(app_key, app_secret))
        self.request_code_url = app_request_code_url
        self.access_token_url = app_access_token_url

    def _prepare_request_code_url_params(self):
        params = super(OAuthLinkedIn, self)._prepare_request_code_url_params()
        params.update({
            'state': '/profile', #TODO: random string (CSRF)
        })
        return params

    def _prepare_access_token_url_params(self):
        params = super(OAuthLinkedIn, self)._prepare_access_token_url_params()
        params.update({
            'grant_type' : 'authorization_code',
        })
        return params

    def get_authorize_url(self, scope='r_basicprofile r_emailaddress'):
        return super(OAuthLinkedIn, self).get_authorize_url(scope=scope)

    def get_profile_info(self, access_token):
        token = json.loads(access_token)
        url = getattr(settings, 'LINKEDIN_PROFILE_URL')
        params = urlencode({'oauth2_access_token': token['access_token'], 'format': 'json'})
        try:
            request = urllib.request.Request(url=url+'?'+params)
            response = urllib.request.urlopen(request)
        except IOError as e:
            contents = e.read()
            raise Exception(contents.decode('utf-8'))
        resp, content =  response.code, response.read()
        if resp != 200:
            raise Exception("Invalid response %s." % resp)        
        return json.loads(content.decode('utf-8'))

    def authenticate(self, linkedin_id):
        return authenticate(linkedin_id=linkedin_id)