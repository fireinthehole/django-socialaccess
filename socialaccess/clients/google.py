import json
from django.contrib.auth import authenticate
from socialaccess.clients import OAuth2Client
from socialaccess.models import GoogleProfile


class OAuth2GoogleClient(OAuth2Client):
    """
    """
    def _prepare_request_code_url_params(self):
        params = super()._prepare_request_code_url_params()
        params.update({
            'access_type': 'online',
            'approval_prompt': 'force',
        })
        return params

    def _prepare_access_token_url_params(self):
        params = super()._prepare_access_token_url_params()
        params.update({
            'grant_type' : 'authorization_code',
        })
        return params

    def _prepare_profile_info_params(self, access_token):
        token = json.loads(access_token)
        return {
            'access_token': token['access_token'],
        }

    def get_profile_info(self, access_token):
        user_data = super().get_profile_info(access_token)
        return {
            'email': user_data['email'],
            'username': user_data['id'],
            'first_name': user_data['given_name'],
            'last_name': user_data['family_name'],
            'id': user_data['id'],
        }

    def create_profile(self, user_data, access_token):
        GoogleProfile.create_profile(user_data, access_token)

    def authenticate(self, identifier):
        return authenticate(google_id=identifier)
