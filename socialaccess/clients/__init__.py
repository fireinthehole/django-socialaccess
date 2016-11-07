import json
import oauth2 as oauth
from urllib.parse import urlparse, urlencode, quote
from django.conf import settings
from django.contrib.sites.models import Site



class OAuth2Client(object):
    """
    """
    def __init__(self, callback_uri): 
        current_site = Site.objects.get_current()
        self.oauth_callback_url = '{protocol}://{site_domain_name}/{callback_uri}'.format(
            protocol=getattr(settings, "DEFAULT_HTTP_PROTOCOL", "http"),
            site_domain_name=current_site.domain.rstrip('/'),
            callback_uri=callback_uri,
        )
        self.access_token_url = None
        self.request_code_url = None

    def _prepare_request_code_url_params(self):
        return {
            'client_id': self.client.consumer.key,
            'response_type': 'code',
            'redirect_uri': self.oauth_callback_url
        }

    def _prepare_access_token_url_params(self):
        return {
            'client_id': self.client.consumer.key,
            'client_secret': self.client.consumer.secret,
            'redirect_uri': self.oauth_callback_url,
        }

    def get_authorize_url(self, scope=''):
        params = self._prepare_request_code_url_params()
        if scope:
            params['scope'] = scope
        return self.request_code_url + '?' + urlencode(params)

    def get_access_token(self, oauth_verifier):
        params = self._prepare_access_token_url_params()
        params['code'] = oauth_verifier

        resp, content = self.client.request(uri=self.access_token_url, method='POST', body=urlencode(params))

        content = content.decode('utf-8')

        if not resp['status'].startswith('2'):
            raise Exception(content)
        return content


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

        resp, content = self.client.request(uri=_url, method=method, body=_params)
        content = json.loads(content.decode("utf-8"))

        if resp['status'] != '200':
            raise Exception(content)
        return content