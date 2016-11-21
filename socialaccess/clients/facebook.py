from urllib.parse import parse_qs
from django.contrib.auth import authenticate
from socialaccess.clients import OAuth2Client
from socialaccess.models import FacebookProfile


class OAuth2FacebookClient(OAuth2Client):
    """
    """
    def _prepare_profile_info_params(self, access_token):
        return {
            'fields': 'id,email,first_name,last_name',
            'access_token': parse_qs(access_token).get('access_token')[0],
        }

    def get_profile_info(self, access_token):
        user_data = super().get_profile_info(access_token)
        return {
            'email': user_data['email'],
            'username': user_data['id'],
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name'],
            'id': user_data['id'],
        }

    def authenticate(self, identifier):
        return authenticate(fb_id=identifier)

    def get_model_class(self):
        return FacebookProfile