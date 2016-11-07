import json
from urllib.parse import parse_qs
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.db import models


class OAuthProfile(models.Model):
    user = models.OneToOneField(getattr(settings, 'AUTH_USER_MODEL', User), related_name='oauth_profile')
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    oauth_token = models.CharField(max_length=2048)


class FacebookProfile(OAuthProfile):
    uid = models.CharField(max_length=128)

    @property
    def access_token(self):
    	return parse_qs(access_token).get('access_token')[0]


class GoogleProfile(OAuthProfile):
    uid = models.CharField(max_length=128)

    @property
    def access_token(self):
        return json.loads(self.oauth_token).get('access_token')


class LinkedinProfile(OAuthProfile):
    uid = models.CharField(max_length=128)
