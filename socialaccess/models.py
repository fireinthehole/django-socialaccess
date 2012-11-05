from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models



class OAuthProfile(models.Model):
    user = models.OneToOneField(User, related_name='oauth_profile')
    site = models.ForeignKey(Site, default=Site.objects.get_current)
    oauth_token = models.CharField(max_length=255)#, editable=False)


class LinkedinProfile(OAuthProfile):
    uid = models.CharField(max_length=80)


class FacebookProfile(OAuthProfile):
    uid = models.CharField(max_length=80)

    @property
    def access_token(self):
    	return self.oauth_token.split('&', 1)[0].split('=', 1)[1]


class TwitterProfile(OAuthProfile):
    uid = models.CharField(max_length=80)


class GoogleProfile(OAuthProfile):
    uid = models.CharField(max_length=80)


class GithubProfile(OAuthProfile):
    uid = models.CharField(max_length=80)