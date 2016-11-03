from urllib.parse import urlparse
import json
import oauth2 as oauth

from urllib.parse import urlencode
from django.conf import settings
from django.contrib.sites.models import Site


class OAuthBaseClient(object):
    def __init__(self, callback_uri): 
        current_site = Site.objects.get_current()
        self.oauth_callback_url = '{protocol}://{site_domain_name}/{callback_uri}'.format(
            protocol=getattr(settings, "DEFAULT_HTTP_PROTOCOL", "http"),
            site_domain_name=current_site.domain.rstrip('/'),
            callback_uri=callback_uri,
        )
        self.access_token_url = None

    def get_profile_info(self, access_token):
        pass

    def call_api(self, url, params, method='GET'):
        _params = ''
        if method in ['GET', 'DELETE']:
            _url = '{url}?{urlencoded_params}'.format(
                url=url,
                urlencoded_params=urlencode(params),
            )
        else:
            _params = urlencode(params)
            _url = url
        resp, content = self.client.request(uri=_url, 
                                            method=method, 
                                            body=_params)
        content = json.loads(content.decode("utf-8"))

        if resp['status'] != '200':
            raise Exception(content['error']['message'])
        return content


class OAuth1Client(OAuthBaseClient):
    def __init__(self, callback_uri): 
        OAuthBaseClient.__init__(self, callback_uri)

    def get_request_token(self, params):
        resp, content = self.client.request(uri=self.request_token_url, 
                                            method="POST", 
                                            body=urlencode(params))
        if resp['status'] != '200':
            raise Exception('Invalid response ({status}).'.format(
                status=resp['status']
            ))
        request_token = dict(urlparse.parse_qsl(content.decode('utf-8')))
        return request_token

    def get_authorize_url(self, oauth_token):
        return '{authorize_url}?oauth_token={oauth_token}'.format(
            authorize_url=self.authorize_url,
            oauth_token=oauth_token,
        )

    def get_access_token(self, oauth_verifier, oauth_token, oauth_token_secret):
        token = oauth.Token(oauth_token, oauth_token_secret)
        token.set_verifier(oauth_verifier)
        self.client.token = token
        resp, content = self.client.request(self.access_token_url, "POST")

        if resp['status'] != '200':
            raise Exception('Invalid response ({status}).'.format(
                status=resp['status']
            ))
        access_token = dict(urlparse.parse_qsl(content.decode('utf-8')))
        return access_token


class OAuth2Client(OAuthBaseClient):
    def __init__(self, callback_uri): 
        OAuthBaseClient.__init__(self, callback_uri)

    def get_authorize_url(self, scope='', extra_params={}):
        url = '{request_code_url}?client_id={client_id}&scope={scope}&response_type=code&redirect_uri={redirect_uri}'.format(
            request_code_url=self.request_code_url,
            client_id=self.client.consumer.key,
            scope=scope,
            redirect_uri=self.oauth_callback_url,
        )
        return url

    def get_access_token(self, oauth_verifier, extra_params={}):
        url = '{access_token_url}?client_id={client_id}&client_secret={client_secret}&code={code}&redirect_uri={redirect_uri}'.format(
            access_token_url=self.access_token_url,
            client_id=self.client.consumer.key,
            client_secret=self.client.consumer.secret,
            code=oauth_verifier,
            redirect_uri=self.oauth_callback_url,
        )
        resp, content = self.client.request(url)
        content = content.decode("utf-8")

        if not resp['status'].startswith('2'):
            content = json.loads(content)
            raise Exception(content['error']['message'])
        return content