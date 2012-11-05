from django.contrib.auth.models import User

from socialaccess.models import *


class LinkedinMixin(object):
    def create_profile(self, user_data, access_token):
        user = User(username   = user_data['first-name']+user_data['last-name']+user_data['id'],
                    first_name = user_data['first-name'],
                    last_name  = user_data['last-name']) #is_active=True
        user.save()
        profile = LinkedinProfile(user=user, 
                                  site=Site.objects.get_current(),
                                  oauth_token=access_token,
                                  uid=user_data['id'])
        profile.save()


class FacebookMixin(object):
    def create_profile(self, user_data, access_token):
        user = User(username   = user_data['username'], 
                    first_name = user_data['first_name'],
                    last_name  = user_data['last_name'],
                    email      = user_data['email'])
        user.save()
        profile = FacebookProfile(user=user, 
                                  site=Site.objects.get_current(),
                                  oauth_token=access_token,
                                  uid=user_data['id'])
        profile.save()


class TwitterMixin(object):
    def create_profile(self, user_data, access_token):
        user = User(username = user_data['username'])
        user.save()
        profile = TwitterProfile(user=user, 
                                 site=Site.objects.get_current(),
                                 oauth_token=access_token,
                                 uid=user_data['id'])
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
                                 uid=user_data['id'])
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
                                 uid=user_data['id'])
        profile.save()