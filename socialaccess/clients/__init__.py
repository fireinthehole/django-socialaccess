import json
import random
import string
import urllib.request
from urllib.parse import urlparse, urlencode, quote
from django.conf import settings
from django.contrib.sites.models import Site


class OAuth2Client(object):
    """
    """
    def __init__(self, app_key, app_secret, request_code_url, access_token_url, scope, callback_uri, profile_url): 
        current_site = Site.objects.get_current()
        self.oauth_callback_url = '{protocol}://{site_domain_name}/{callback_uri}'.format(
            protocol=getattr(settings, "DEFAULT_HTTP_PROTOCOL", "http"),
            site_domain_name=current_site.domain.rstrip('/'),
            callback_uri=callback_uri,
        )
        self.app_key = app_key
        self.app_secret = app_secret
        self.request_code_url = request_code_url
        self.access_token_url = access_token_url
        self.scope = scope
        self.state = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(32))
        self.profile_url = profile_url

    def _prepare_request_code_url_params(self):
        return {
            'client_id': self.app_key,
            'response_type': 'code',
            'redirect_uri': self.oauth_callback_url,
            'scope': self.scope,
            'state': self.state,
        }

    def _prepare_access_token_url_params(self):
        return {
            'client_id': self.app_key,
            'client_secret': self.app_secret,
            'redirect_uri': self.oauth_callback_url,
        }

    def _prepare_profile_info_params(self, access_token):
        raise NotImplementedError('Please Implement this method')

    def get_authorize_url(self):
        params = self._prepare_request_code_url_params()
        authorize_url = self.request_code_url + '?' + urlencode(params)
        return authorize_url

    def get_access_token(self, oauth_verifier):
        params = self._prepare_access_token_url_params()
        params['code'] = oauth_verifier

        req = urllib.request.Request(self.access_token_url, bytearray(urlencode(params), 'utf-8'))
        handle = urllib.request.urlopen(req, timeout=15)
        status, content = handle.getcode(), handle.read()
        content = content.decode('utf-8')

        if not str(status).startswith('2'):
            raise Exception(content)
        return content

    def get_profile_info(self, access_token):
        params = self._prepare_profile_info_params(access_token)
        url = self.profile_url + '?' + urlencode(params)

        req = urllib.request.Request(url)
        handle = urllib.request.urlopen(req, timeout=15)
        status, content = handle.getcode(), handle.read()

        content = content.decode('utf-8')

        if status != 200:
            raise Exception(content)
        return json.loads(content)

    def get_model_class(self):
        raise NotImplementedError('Please Implement this method')

    def create_profile(self, user_data, access_token):
        model_cls = self.get_model_class()
        model_cls.create_profile(user_data, access_token)

    def update_access_token(self, email, access_token):
        model_cls = self.get_model_class()
        extended_user = model_cls.objects.get(user__email=email)
        if extended_user.oauth_token != access_token:
            extended_user.oauth_token = access_token
            extended_user.save()