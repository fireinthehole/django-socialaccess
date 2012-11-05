from django.contrib.auth.models import User

from socialaccess.models import LinkedinProfile, FacebookProfile, TwitterProfile, GoogleProfile


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


class OAuthTwitterBackend(OAuthBackend):
    def authenticate(self, twitter_id):
        try:
            profile = TwitterProfile.objects.get(uid=twitter_id)
            return profile.user
        except TwitterProfile.DoesNotExist:
            return None  


class OAuthGoogleBackend(OAuthBackend):
    def authenticate(self, google_id):
        try:
            profile = GoogleProfile.objects.get(uid=google_id)
            return profile.user
        except GoogleProfile.DoesNotExist:
            return None 


class OAuthGithubBackend(OAuthBackend):
    def authenticate(self, github_id):
        try:
            profile = GithubProfile.objects.get(uid=github_id)
            return profile.user
        except GithubProfile.DoesNotExist:
            return None 