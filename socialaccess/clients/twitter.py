import oauth2 as oauth
import urllib
import json

from django.conf import settings
from django.contrib.auth import authenticate

from socialaccess.clients import OAuth1Client


class OAuthTwitter(OAuth1Client):
    def __init__(self, callback_uri='socialaccess/twittercallback'):
        OAuth1Client.__init__(self, callback_uri)
        self.client             = oauth.Client(oauth.Consumer(
                                                        getattr(settings, 'TWITTER_KEY', ''),
                                                        getattr(settings, 'TWITTER_SECRET', '')))
        self.request_token_url  = getattr(settings, 'TWITTER_REQUEST_TOKEN_URL', '')
        self.authorize_url      = getattr(settings, 'TWITTER_AUTHORIZE_URL', '')
        self.access_token_url   = getattr(settings, 'TWITTER_ACCESS_TOKEN_URL','')

    
    def get_profile_info(self, access_token):
        return  {
                    'id' : access_token['user_id'],
                    'username' : access_token['screen_name'],
                }


    def authenticate(self, twitter_id):
        return authenticate(twitter_id=twitter_id)