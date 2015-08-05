import oauth2 as oauth

from django.conf import settings
from django.contrib.auth import authenticate

from socialaccess.clients import OAuth1Client


class OAuthTwitter(OAuth1Client):
    def __init__(self, callback_uri='socialaccess/twittercallback'):
        try:
            app_key = getattr(settings, 'TWITTER_KEY')
            app_secret = getattr(settings, 'TWITTER_SECRET')
            app_request_token_url = getattr(settings, 'TWITTER_REQUEST_TOKEN_URL')
            app_authorize_url     = getattr(settings, 'TWITTER_AUTHORIZE_URL')
            app_access_token_url  = getattr(settings, 'TWITTER_ACCESS_TOKEN_URL')
        except AttributeError:
            raise Exception('One of these parameters is missing in settings.py: '\
                            'TWITTER_KEY / TWITTER_SECRET / TWITTER_REQUEST_TOKEN_URL / TWITTER_AUTHORIZE_URL / TWITTER_ACCESS_TOKEN_URL')

        OAuth1Client.__init__(self, callback_uri)
        self.client            = oauth.Client(oauth.Consumer(app_key, app_secret))
        self.request_token_url = app_request_token_url
        self.authorize_url     = app_authorize_url
        self.access_token_url  = app_access_token_url

    
    def get_profile_info(self, access_token):
        return  {
                    'id' : access_token['user_id'],
                    'username' : access_token['screen_name'],
                }


    def authenticate(self, twitter_id):
        return authenticate(twitter_id=twitter_id)