import urlparse 
import urllib
import oauth2 as oauth

from django.conf import settings
from django.contrib.sites.models import Site



class OAuthBaseClient(object):
    def __init__(self, callback_uri): 
        current_site = Site.objects.get_current()
        protocol = getattr(settings, "DEFAULT_HTTP_PROTOCOL", "http")
        site_url = u"%s://%s" % (protocol, current_site.domain)
        self.oauth_callback_url = u"%s/%s" % (site_url, callback_uri)


    def get_profile_info(self, access_token):
        pass


    def call_api(self, url, params, method='GET'):
        _params = ''
        if method in ['GET', 'DELETE']:
            _url = u'%s?%s' % (url, urllib.urlencode(params))
        else:
            _params = urllib.urlencode(params)
            _url = url
        resp, content = self.client.request(uri=_url, 
                                            method=method, 
                                            body=_params)
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        return str(content)


class OAuth1Client(OAuthBaseClient):
    def __init__(self, callback_uri): 
        OAuthBaseClient.__init__(self, callback_uri)

    
    def get_request_token(self, params):
        resp, content = self.client.request(uri=self.request_token_url, 
                                            method="POST", 
                                            body=urllib.urlencode(params))
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        request_token = dict(urlparse.parse_qsl(content))
        return request_token


    def get_authorize_url(self, oauth_token):
        return u"%s?oauth_token=%s" % (self.authorize_url, oauth_token)


    def get_access_token(self, oauth_verifier, oauth_token, oauth_token_secret):
        token = oauth.Token(oauth_token, oauth_token_secret)
        token.set_verifier(oauth_verifier)
        self.client.token = token
        resp, content = self.client.request(self.access_token_url, "POST")
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        return dict(urlparse.parse_qsl(content))


    
class OAuth2Client(OAuthBaseClient):
    def __init__(self, callback_uri): 
        OAuthBaseClient.__init__(self, callback_uri)


    def get_authorize_url(self, scope=None, extra_params=None):
        url = u"%s?client_id=%s&redirect_uri=%s" % (self.request_code_url,
                                                    self.client.consumer.key,
                                                    self.oauth_callback_url)
        if scope:
            url += '&scope=%s' % scope
        if extra_params:
            url += extra_params
        return url


    def get_access_token(self, oauth_verifier, extra_params={}):
        access_params = {
            'client_id'     : self.client.consumer.key,
            'client_secret' : self.client.consumer.secret,
            'redirect_uri'  : self.oauth_callback_url,
            'code'          : oauth_verifier
        }
        if extra_params:
            access_params.update(extra_params)
        resp, content = self.client.request(uri=self.access_token_url, 
                                             method="POST", 
                                             body=urllib.urlencode(access_params))
        if resp['status'] != '200':
            raise Exception("Invalid response %s." % resp['status'])
        return unicode(content)
