# -*- coding: utf-8 -*-
from urllib.parse import urlparse
import json
import oauth2 as oauth

from urllib.parse import urlencode
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
            _url = u'%s?%s' % (url, urlencode(params))
        else:
            _params = urlencode(params)
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
                                            body=urlencode(params))
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

    def get_authorize_url(self, scope='', extra_params={}):
        url = u'{}?client_id={}&scope={}&response_type=code&redirect_uri={}'.format(
            self.request_code_url,
            self.client.consumer.key,
            scope,
            self.oauth_callback_url
        )
        return url

    def get_access_token(self, oauth_verifier, extra_params={}):
        url = u'{}?client_id={}&client_secret={}&code={}&redirect_uri={}'.format(
            self.access_token_url,
            self.client.consumer.key,
            self.client.consumer.secret,
            oauth_verifier,
            self.oauth_callback_url
        )
        resp, content = self.client.request(url)
        
        if not resp['status'].startswith('2'):
            if resp['status'].startswith('4'):
                err_details = json.loads(content)
                error = err_details.get('error')
                if error:
                    raise Exception(error.get('message'))
            raise Exception('An error occured')
        return content