import json
import oauth2 as oauth
import urllib.request
from urllib.parse import urlencode
from django.conf import settings
from django.contrib.auth import authenticate
from socialaccess.clients import OAuth2Client


class OAuthGoogle(OAuth2Client):
    def __init__(self, callback_uri='socialaccess/googlecallback'):
        app_key = getattr(settings, 'GOOGLE_KEY')
        app_secret = getattr(settings, 'GOOGLE_SECRET')
        app_request_code_url = getattr(settings, 'GOOGLE_REQUEST_CODE_URL')
        app_access_token_url = getattr(settings, 'GOOGLE_ACCESS_TOKEN_URL')

        OAuth2Client.__init__(self, callback_uri)
        self.client  = oauth.Client(oauth.Consumer(app_key, app_secret))
        self.request_code_url = app_request_code_url
        self.access_token_url = app_access_token_url
    
    def _prepare_request_code_url_params(self):
        params = super(OAuthGoogle, self)._prepare_request_code_url_params()
        params.update({
            'state': '/profile',
            'access_type': 'online',
            'approval_prompt': 'force',
        })
        return params

    def _prepare_access_token_url_params(self):
        params = super(OAuthGoogle, self)._prepare_access_token_url_params()
        params.update({
            'grant_type' : 'authorization_code',
        })
        return params

    def get_authorize_url(self, scope='https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile'):
        return super(OAuthGoogle, self).get_authorize_url(scope=scope)

    def get_profile_info(self, access_token):
        token = json.loads(access_token)
        url = getattr(settings, 'GOOGLE_PROFILE_URL')
        params = urlencode({'access_token': token['access_token']})
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

    def authenticate(self, google_id):
        return authenticate(google_id=google_id)
