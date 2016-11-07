import json
from django.views.generic.base import View
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import login, get_user_model

from socialaccess.clients import OAuth2Client
from socialaccess.clients.facebook import OAuthFacebook
from socialaccess.clients.linkedin import OAuthLinkedIn
from socialaccess.clients.google import OAuthGoogle
from socialaccess.mixins import (LinkedinMixin, FacebookMixin, GoogleMixin)


User = get_user_model()


class AbstractOAuthConnectView(View):
    """
    """
    client_class = None

    @property
    def authorize_url(self):
        """
            Build the authorization url
        """
        client = self.client_class()
        return client.get_authorize_url()

    def get(self, request):
        return redirect(self.authorize_url)


class AbstractOAuthCallbackView(View):
    """
    """
    client_class = None

    def get(self, request):
        oauth_verifier = request.GET.get('code')
        error_message = request.GET.get('error_message')
        client = self.client_class()
        
        if error_message:
            return HttpResponse('An error occured on the callback step: {}'.format(error_message), status=400)

        # Get the access token
        try:
            access_token = client.get_access_token(oauth_verifier=oauth_verifier)
        except Exception as e:
            return HttpResponse(e, status=400)

        # Get the user profile information
        try:
            # Request the oauth provider API to get the user's profile info
            user_data = client.get_profile_info(access_token)
        except Exception as e:
            return HttpResponse(e, status=400)

        # Try to authenticate a user already registered with oauth
        user = client.authenticate(user_data['id'])

        if user is None:
            try:
                # Look for a user alreday registered without oauth
                user = User.objects.get(email=user_data.get('email'))
                
                # Refuse to authenticate if the user exists
                return HttpResponse('User {id} already exists without social account association. Please authenticate using the login form.'.format(
                    id=user_data.get('email')),
                    status=400
                )
            except User.DoesNotExist:
                # Create a new account with social account association
                self.create_profile(user_data, access_token)
                user = client.authenticate(user_data['id'])
        
        login(request, user)
        return redirect('/')


class FacebookConnectView(AbstractOAuthConnectView):
    client_class = OAuthFacebook


class FacebookCallbackView(AbstractOAuthCallbackView, FacebookMixin):
    client_class = OAuthFacebook


class GoogleConnectView(AbstractOAuthConnectView):
    client_class = OAuthGoogle


class GoogleCallbackView(AbstractOAuthCallbackView, GoogleMixin):
    client_class = OAuthGoogle


class LinkedinConnectView(AbstractOAuthConnectView):
    client_class = OAuthLinkedIn


class LinkedinCallbackView(AbstractOAuthCallbackView, LinkedinMixin):
    client_class = OAuthLinkedIn
