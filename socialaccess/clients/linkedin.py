import oauth2 as oauth
import urllib
import json

from lxml import etree
from cStringIO import StringIO

from django.conf import settings
from django.contrib.auth import authenticate

from socialaccess.clients import OAuth1Client


class OAuthLinkedIn(OAuth1Client):
    def __init__(self, callback_uri='socialaccess/linkedincallback'):
        OAuth1Client.__init__(self, callback_uri)
        self.client             = oauth.Client(oauth.Consumer(
                                                        getattr(settings, 'LINKEDIN_KEY', ''),
                                                        getattr(settings, 'LINKEDIN_SECRET', '')))
        self.request_token_url  = getattr(settings, 'LINKEDIN_REQUEST_TOKEN_URL', 'https://api.linkedin.com/uas/oauth/requestToken')
        self.authorize_url      = getattr(settings, 'LINKEDIN_AUTHORIZE_URL', 'https://api.linkedin.com/uas/oauth/authorize')
        self.access_token_url   = getattr(settings, 'LINKEDIN_ACCESS_TOKEN_URL','https://api.linkedin.com/uas/oauth/accessToken')

    
    def get_profile_info(self, access_token):
        url = getattr(settings, 'LINKEDIN_PROFILE_URL', 'http://api.linkedin.com/v1/people/')
        url += '~:(id,first-name,last-name,headline,industry)'
        self.client.token = oauth.Token(key=access_token['oauth_token'], secret=access_token['oauth_token_secret'])
        resp, content = self.client.request(url)
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        tree = etree.parse(StringIO(content))
        person = tree.xpath("//person")[0]
        data = {
                'id'                            : person.xpath("id")[0].text,
                'first-name'                    : person.xpath("first-name")[0].text,
                'last-name'                     : person.xpath("last-name")[0].text,
                'headline'                      : person.xpath("headline")[0].text,
                'industry'                      : person.xpath("industry")[0].text,
               }
        return data

    def authenticate(self, linkedin_id):
        return authenticate(linkedin_id=linkedin_id)