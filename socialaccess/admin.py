from django.contrib import admin
from socialaccess.models import OAuthProfile, LinkedinProfile, FacebookProfile, GoogleProfile, GithubProfile


admin.site.register(OAuthProfile)
admin.site.register(LinkedinProfile)
admin.site.register(FacebookProfile)
admin.site.register(GoogleProfile)
admin.site.register(GithubProfile)