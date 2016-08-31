# -*- coding: utf-8 -*-
import random
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from socialaccess.models import (
    FacebookProfile, GoogleProfile, LinkedinProfile, TwitterProfile, GithubProfile
)

User = get_user_model()


class LinkedinMixin(object):
    def create_profile(self, user_data, access_token):
        print(user_data)
        user = User(username = '{}{}'.format(user_data['firstName'], user_data['lastName']),
                    first_name = user_data['firstName'], 
                    last_name = user_data['lastName']
        )
        user.save()
        profile = LinkedinProfile(user=user, 
                                  site=Site.objects.get_current(),
                                  oauth_token=access_token,
                                  uid=user_data['id']
        )
        profile.save()


class FacebookMixin(object):
    def create_profile(self, user_data, access_token):
        user = User(email = user_data['email'], 
                    first_name = user_data['first_name'],
                    last_name  = user_data['last_name']
        )
        user.save()
        profile = FacebookProfile(user=user, 
                                  site=Site.objects.get_current(),
                                  oauth_token=access_token,
                                  uid=user_data['id']
        )
        profile.save()


class TwitterMixin(object):
    def create_profile(self, user_data, access_token):
        user = User(username = user_data['username'])
        user.save()
        profile = TwitterProfile(user=user, 
                                 site=Site.objects.get_current(),
                                 oauth_token=access_token,
                                 uid=user_data['id']
        )
        profile.save()


class GoogleMixin(object):
    def create_profile(self, user_data, access_token):
        user = User(username   = user_data['name'],
                    first_name = user_data['given_name'],
                    last_name  = user_data['family_name'],
                    email      = user_data['email'])
        user.save()
        profile = GoogleProfile( user=user, 
                                 site=Site.objects.get_current(),
                                 oauth_token=access_token,
                                 uid=user_data['id']
        )
        profile.save()


class GithubMixin(object):
    def create_profile(self, user_data, access_token):
        user = User(username   = user_data['name'],
                    first_name = user_data['given_name'],
                    last_name  = user_data['family_name'],
                    email      = user_data['email'])
        user.save()
        profile = GithubProfile( user=user, 
                                 site=Site.objects.get_current(),
                                 oauth_token=access_token,
                                 uid=user_data['id']
        )
        profile.save()