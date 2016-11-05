from django.views.generic.base import View
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import login, get_user_model

from socialaccess.clients import (OAuth1Client, OAuth2Client)
from socialaccess.clients.facebook import OAuthFacebook
from socialaccess.clients.linkedin import OAuthLinkedIn
from socialaccess.clients.twitter import OAuthTwitter
from socialaccess.clients.google import OAuthGoogle
from socialaccess.clients.github import OAuthGithub
from socialaccess.mixins import (LinkedinMixin, FacebookMixin, TwitterMixin, GoogleMixin, GithubMixin)
from socialaccess.exceptions import NotAllowedException


User = get_user_model()


class AbstractOAuthConnect(View):
    client_class = None

    def request_code(self):
        """
            Get the request_token if the protocol of AbstractOAuthConnect subclasses needs it and put it into the request session
        """
        pass

    @property
    def authorize_url(self):
        """
            Build the authorization url
        """
        request_token = self.request.session.get('request_token', None)
        oauth_token = request_token['oauth_token'] if request_token else None
        client = self.client_class()

        if isinstance(client, OAuth1Client):
            return client.get_authorize_url(oauth_token)
        return client.get_authorize_url()

    def get(self, request):
        try:
            self.request_code()
            return redirect(self.authorize_url)
        except NotAllowedException as e:
            return HttpResponse('Unauthorized: {}'.format(e), status=401)


class AbstractOAuthCallback(View):
    client_class = None
    oauth_verifier_name = None

    def get(self, request):
        oauth_verifier = request.GET.get(self.oauth_verifier_name)
        error_message = request.GET.get('error_message')
        request_token  = request.session.get('request_token')
        client = self.client_class()
        
        if error_message:
            return HttpResponse(error_message, status=400)

        try:
            if isinstance(client, OAuth1Client):
                access_token = client.get_access_token(
                    oauth_verifier = oauth_verifier, 
                    oauth_token = request_token['oauth_token'],
                    oauth_token_secret = request_token['oauth_token_secret']
                )
            else:
                access_token = client.get_access_token(oauth_verifier=oauth_verifier)

            # Request the oauth provider API to get the user's profile info
            user_data = client.get_profile_info(access_token)
        except Exception as e:
            return HttpResponse(e, status=401)

        # Try to authenticate a user already registered with oauth
        user = client.authenticate(user_data['id'])

        if user is None:
            if 'email' not in user_data:
                return HttpResponse('Cannot create user, email field has not been authorized', status=401)
            try:
                # Look for a user alreday registered without oauth
                user = User.objects.get(email=user_data.get('email'))
                
                # Refuse to authenticate if the user exists
                return HttpResponse('User {id} already exists without social account association. Please authenticate using the login form.'.format(
                    id=user_data.get('email')),
                    status=401
                )
            except User.DoesNotExist:
                # Create a new account with social account association
                self.create_profile(user_data, access_token)
                user = client.authenticate(user_data['id'])
        
        login(request, user)
        print(user, user.is_authenticated(), request.user.is_authenticated())
        return redirect('/')


class LinkedinConnect(AbstractOAuthConnect):
    client_class = OAuthLinkedIn

    def request_code(self):
        try:
            client = LinkedinConnect.client_class()
            self.request.session['request_token'] = client.get_request_token({'oauth_callback': client.oauth_callback_url})
        except Exception as e:
            raise NotAllowedException(e)


class LinkedinCallback(AbstractOAuthCallback, LinkedinMixin):
    client_class = OAuthLinkedIn
    oauth_verifier_name = 'oauth_verifier'


class FacebookConnect(AbstractOAuthConnect):
    client_class = OAuthFacebook


class FacebookCallback(AbstractOAuthCallback, FacebookMixin):
    client_class = OAuthFacebook
    oauth_verifier_name = 'code'


class TwitterConnect(AbstractOAuthConnect):
    client_class = OAuthTwitter

    def request_code(self):
        try:
            client = TwitterConnect.client_class()
            self.request.session['request_token'] = client.get_request_token({'oauth_callback': client.oauth_callback_url})
        except Exception as e:
            raise NotAllowedException(e)

class TwitterCallback(AbstractOAuthCallback, TwitterMixin):
    client_class = OAuthTwitter
    oauth_verifier_name = 'oauth_verifier'


class GoogleConnect(AbstractOAuthConnect):
    client_class = OAuthGoogle


class GoogleCallback(AbstractOAuthCallback, GoogleMixin):
    client_class = OAuthGoogle
    oauth_verifier_name = 'code'


class GithubConnect(AbstractOAuthConnect):
    cliclient_classent = OAuthGithub


class GithubCallback(AbstractOAuthCallback, GithubMixin):
    client_class = OAuthGithub
    oauth_verifier_name = 'code'
