import json
from django.contrib.auth import authenticate
from socialaccess.clients import OAuth2Client
from socialaccess.models import LinkedinProfile


class OAuth2LinkedInClient(OAuth2Client):
    """
    """
    def _prepare_access_token_url_params(self):
        params = super()._prepare_access_token_url_params()
        params.update({
            'grant_type' : 'authorization_code',
        })
        return params

    def _prepare_profile_info_params(self, access_token):
        token = json.loads(access_token)
        return {
            'oauth2_access_token': token['access_token'],
            'format': 'json',
        }

    def get_profile_info(self, access_token):
        user_data = super().get_profile_info(access_token)
        return {
            'email': user_data['emailAddress'],
            'username': user_data['id'],
            'first_name': user_data['firstName'],
            'last_name': user_data['lastName'],
            'id': user_data['id'],
        }

    def authenticate(self, identifier):
        return authenticate(linkedin_id=identifier)

    def get_model_class(self):
        return LinkedinProfile