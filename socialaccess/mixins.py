import random
from django.conf import settings
from django.db import transaction
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from socialaccess.models import (
    FacebookProfile, GoogleProfile, LinkedinProfile
)


User = get_user_model()


class BaseSocialMixin(object):
    """
    """
    PROFILE_MODEL_CLASS = None

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    FIRST_NAME_FIELD = 'first_name'
    LAST_NAME_FIELD = 'last_name'
    UID_FIELD = 'id'

    def create_profile(self, user_data, access_token):
        """
        """
        site = Site.objects.get_current()

        try:
            with transaction.atomic():
                first_name = user_data.get(self.FIRST_NAME_FIELD)
                last_name = user_data.get(self.LAST_NAME_FIELD)
                email = user_data.get(self.EMAIL_FIELD, '{first_name}.{last_name}@{domain}'.format(
                    first_name=first_name,
                    last_name=last_name,
                    domain=site.domain,
                ))
                username = user_data.get(self.UID_FIELD)

                user = User(
                    email = email, 
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                )
                user.save()

                profile_class = self.PROFILE_MODEL_CLASS

                profile = profile_class(
                    user = user, 
                    site = site,
                    oauth_token = access_token,
                    uid = user_data[self.UID_FIELD],
                )
                profile.save()
        except IntegrityError:
            transaction.rollback()
            raise

class FacebookMixin(BaseSocialMixin):
    """
    """
    PROFILE_MODEL_CLASS = FacebookProfile
    

class GoogleMixin(BaseSocialMixin):
    """
    """
    PROFILE_MODEL_CLASS = GoogleProfile

    FIRST_NAME_FIELD = 'given_name'
    LAST_NAME_FIELD = 'family_name'


class LinkedinMixin(BaseSocialMixin):
    """
    """
    PROFILE_MODEL_CLASS = LinkedinProfile

    EMAIL_FIELD = 'emailAddress'
    FIRST_NAME_FIELD = 'firstName'
    LAST_NAME_FIELD = 'lastName'
