from django.conf import settings
from socialaccess.clients.facebook import OAuth2FacebookClient
from socialaccess.clients.google import OAuth2GoogleClient
from socialaccess.clients.linkedin import OAuth2LinkedInClient
from socialaccess.clients.github import OAuth2GitHubClient


class FacebookViewMixin(object):
    """
    """
    def get_oauth2_client(self):
        app_key = getattr(settings, 'FACEBOOK_KEY')
        app_secret = getattr(settings, 'FACEBOOK_SECRET')
        request_code_url = getattr(settings, 'FACEBOOK_REQUEST_CODE_URL')
        access_token_url = getattr(settings, 'FACEBOOK_ACCESS_TOKEN_URL')
        scope = getattr(settings, 'FACEBOOK_SCOPE')
        profile_url = getattr(settings, 'FACEBOOK_PROFILE_URL')
        callback_uri = 'socialaccess/fbcallback'
        client = OAuth2FacebookClient(app_key, app_secret, request_code_url, access_token_url, scope, callback_uri, profile_url)
        return client
    

class GoogleViewMixin(object):
    """
    """
    def get_oauth2_client(self):
        app_key = getattr(settings, 'GOOGLE_KEY')
        app_secret = getattr(settings, 'GOOGLE_SECRET')
        request_code_url = getattr(settings, 'GOOGLE_REQUEST_CODE_URL')
        access_token_url = getattr(settings, 'GOOGLE_ACCESS_TOKEN_URL')
        scope = getattr(settings, 'GOOGLE_SCOPE')
        profile_url = getattr(settings, 'GOOGLE_PROFILE_URL')
        callback_uri = 'socialaccess/googlecallback'
        client = OAuth2GoogleClient(app_key, app_secret, request_code_url, access_token_url, scope, callback_uri, profile_url)
        return client


class LinkedinViewMixin(object):
    """
    """
    def get_oauth2_client(self):
        app_key = getattr(settings, 'LINKEDIN_KEY')
        app_secret = getattr(settings, 'LINKEDIN_SECRET')
        request_code_url = getattr(settings, 'LINKEDIN_REQUEST_CODE_URL')
        access_token_url  = getattr(settings, 'LINKEDIN_ACCESS_TOKEN_URL')
        scope = getattr(settings, 'LINKEDIN_SCOPE')
        profile_url = getattr(settings, 'LINKEDIN_PROFILE_URL')
        callback_uri = 'socialaccess/linkedincallback'
        client = OAuth2LinkedInClient(app_key, app_secret, request_code_url, access_token_url, scope, callback_uri, profile_url)
        return client


class GithubViewMixin(object):
    """
    """
    def get_oauth2_client(self):
        app_key = getattr(settings, 'GITHUB_KEY')
        app_secret = getattr(settings, 'GITHUB_SECRET')
        request_code_url = getattr(settings, 'GITHUB_REQUEST_CODE_URL')
        access_token_url  = getattr(settings, 'GITHUB_ACCESS_TOKEN_URL')
        scope = getattr(settings, 'GITHUB_SCOPE')
        profile_url = getattr(settings, 'GITHUB_PROFILE_URL')
        callback_uri = 'socialaccess/githubcallback'
        client = OAuth2GitHubClient(app_key, app_secret, request_code_url, access_token_url, scope, callback_uri, profile_url)
        return client

