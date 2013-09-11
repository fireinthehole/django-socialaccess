from django.views.generic.base import View
from django.shortcuts import redirect
from django.http import Http404
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import login

from socialaccess.clients import OAuth1Client, OAuth2Client
from socialaccess.clients.facebook import OAuthFacebook
from socialaccess.clients.linkedin import OAuthLinkedIn
from socialaccess.clients.twitter import OAuthTwitter
from socialaccess.clients.google import OAuthGoogle
from socialaccess.clients.github import OAuthGithub
from socialaccess.mixins import LinkedinMixin, FacebookMixin, TwitterMixin, GoogleMixin, GithubMixin



#TODO: handle token expiration/renewing

class OAuthConnect(View):
    client = None

    def request_code(self):
        """
            Get the request_token if the protocol of OAuthConnect subclasses needs it and put it into the request session
        """
        pass

    @property
    def authorize_url(self):
        """
            Build the authorization url
        """
        request_token = self.request.session.get('request_token', None)
        oauth_token = request_token['oauth_token'] if request_token else None
        if isinstance(self.client, OAuth1Client):
            return self.client.get_authorize_url(oauth_token)
        return self.client.get_authorize_url()

    def get(self, request):
        try:
            self.request_code()
            return redirect(self.authorize_url)
        except:
            raise Http404


class OAuthCallback(View):
    client = None
    oauth_verifier_name = None

    def get(self, request):
        oauth_verifier = request.GET.get(self.oauth_verifier_name)
        request_token  = request.session.get('request_token')
        
        try:
            if isinstance(self.client, OAuth1Client):
                access_token = self.client.get_access_token(oauth_verifier, request_token['oauth_token'], request_token['oauth_token_secret'])
            else:
                access_token = self.client.get_access_token(oauth_verifier)
                
            user_data = self.client.get_profile_info(access_token)
        except Exception, e:
            #print str(e)
            raise Http404

        user = self.client.authenticate(user_data['id'])
        if user is None:
            self.create_profile(user_data, access_token)
            user = self.client.authenticate(user_data['id'])
        
        login(request, user)
        return redirect(reverse('home'))


class LinkedinConnect(OAuthConnect):
    client = OAuthLinkedIn()

    def request_code(self):
        self.request.session['request_token'] = self.client.get_request_token({'oauth_callback': self.client.oauth_callback_url})


class LinkedinCallback(OAuthCallback, LinkedinMixin):
    client = OAuthLinkedIn()
    oauth_verifier_name = 'oauth_verifier'


class FacebookConnect(OAuthConnect):
    client = OAuthFacebook()


class FacebookCallback(OAuthCallback, FacebookMixin):
    client = OAuthFacebook()
    oauth_verifier_name = 'code'


class TwitterConnect(OAuthConnect):
    client = OAuthTwitter()

    def request_code(self):
        self.request.session['request_token'] = self.client.get_request_token({'oauth_callback': self.client.oauth_callback_url})


class TwitterCallback(OAuthCallback, TwitterMixin):
    client = OAuthTwitter()
    oauth_verifier_name = 'oauth_verifier'


class GoogleConnect(OAuthConnect):
    client = OAuthGoogle()


class GoogleCallback(OAuthCallback, GoogleMixin):
    client = OAuthGoogle()
    oauth_verifier_name = 'code'


class GithubConnect(OAuthConnect):
    """under construction DNS needed"""
    client = OAuthGithub()


class GithubCallback(OAuthCallback, GithubMixin):
    """under construction"""
    client = OAuthGithub()
    oauth_verifier_name = 'code'
