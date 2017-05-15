from urllib.parse import parse_qs
from django.contrib.auth import authenticate
from django.contrib.sites.models import Site
from socialaccess.clients import OAuth2Client
from socialaccess.models import GithubProfile


class OAuth2GitHubClient(OAuth2Client):
    """
    """
    def _prepare_access_token_url_params(self):
        params = super()._prepare_access_token_url_params()
        params.update({
            'grant_type' : 'authorization_code',
        })
        return params

    def _prepare_profile_info_params(self, access_token):
        return {
            'access_token': parse_qs(access_token).get('access_token')[0],
        }

    def get_profile_info(self, access_token):
        user_data = super().get_profile_info(access_token)
        name = user_data['name'].split(' ')
        first_name, last_name = name[0:2] if len(name) == 2 else (name[0], '')
        site = Site.objects.get_current()
        return {
            'email': user_data['email'] or 'github_{id}@{domain}'.format(id=user_data['id'], domain=site.name),
            'username': user_data['id'],
            'first_name': first_name,
            'last_name': last_name,
            'id': user_data['id'],
        }

    def authenticate(self, identifier):
        return authenticate(github_id=identifier)

    def get_model_class(self):
        return GithubProfile
