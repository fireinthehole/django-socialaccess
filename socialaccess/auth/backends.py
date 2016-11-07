from django.contrib.auth import get_user_model
from socialaccess.models import (
    LinkedinProfile, FacebookProfile, GoogleProfile
)

User = get_user_model()


class OAuthBackend(object):
    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self):
        pass

    def get_user(self, user_id):
        user = None
        try:
            user = User.objects.get(pk=user_id)
        except:
            pass
        return user


class OAuthLinkedinBackend(OAuthBackend):
    def authenticate(self, linkedin_id):
        try:
            profile = LinkedinProfile.objects.get(uid=linkedin_id)
            return profile.user
        except LinkedinProfile.DoesNotExist:
            return None      


class OAuthFacebookBackend(OAuthBackend):
    def authenticate(self, fb_id):
        try:
            profile = FacebookProfile.objects.get(uid=fb_id)
            return profile.user
        except FacebookProfile.DoesNotExist:
            return None 


class OAuthGoogleBackend(OAuthBackend):
    def authenticate(self, google_id):
        try:
            profile = GoogleProfile.objects.get(uid=google_id)
            return profile.user
        except GoogleProfile.DoesNotExist:
            return None 
