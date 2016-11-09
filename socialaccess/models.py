import json
from urllib.parse import parse_qs
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.conf import settings
from django.db import models
from django.db import transaction
from django.db import IntegrityError


UserProfile = getattr(settings, 'AUTH_USER_MODEL')


class ProfileModelMixin(object):
    """
    """
    @classmethod
    def create_profile(cls, user_data, access_token):
        """
        Create a social profile
        """
        site = Site.objects.get_current()

        try:
            with transaction.atomic():
                first_name = user_data.get('first_name')
                last_name = user_data.get('last_name')
                email = user_data.get('email')
                username = user_data.get('username')
                uid = user_data.get('id')

                user_cls = get_user_model()
                user = user_cls(
                    email = email, 
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                )
                user.save()

                profile = cls(
                    user = user, 
                    site = site,
                    oauth_token = access_token,
                    uid = uid,
                )
                profile.save()
        except IntegrityError:
            transaction.rollback()
            raise


class OAuthProfile(models.Model):
    """
    Base model for social profiles
    """
    user = models.OneToOneField(UserProfile, related_name='oauth_user')
    site = models.ForeignKey(Site, default=settings.SITE_ID)
    oauth_token = models.CharField(max_length=2048)


class FacebookProfile(OAuthProfile, ProfileModelMixin):
    """
    """
    uid = models.CharField(max_length=128)

    @property
    def access_token(self):
    	return parse_qs(self.oauth_token).get('access_token')[0]


class GoogleProfile(OAuthProfile, ProfileModelMixin):
    """
    """
    uid = models.CharField(max_length=128)

    @property
    def access_token(self):
        return json.loads(self.oauth_token).get('access_token')


class LinkedinProfile(OAuthProfile, ProfileModelMixin):
    """
    """
    uid = models.CharField(max_length=128)

    @property
    def access_token(self):
        return json.loads(self.oauth_token).get('access_token')
