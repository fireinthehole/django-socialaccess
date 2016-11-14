from django.conf.urls import url

from socialaccess.views import (
    LinkedinConnectView, LinkedinCallbackView,
    FacebookConnectView, FacebookCallbackView,
    GoogleConnectView, GoogleCallbackView,
    GithubConnectView, GithubCallbackView,
)


urlpatterns = [
    url(r'^fblogin/$', FacebookConnectView.as_view(), name='fb_connect'),
    url(r'^fbcallback/$', FacebookCallbackView.as_view(), name='fb_callback'),

    url(r'^linkedinlogin/$', LinkedinConnectView.as_view(), name='linkedin_connect'),
    url(r'^linkedincallback/$', LinkedinCallbackView.as_view(), name='linkedin_callback'),

    url(r'^googlelogin/$', GoogleConnectView.as_view(), name='google_connect'),
    url(r'^googlecallback/$', GoogleCallbackView.as_view(), name='google_callback'),

    url(r'^githublogin/$', GithubConnectView.as_view(), name='github_connect'),
    url(r'^githubcallback/$', GithubCallbackView.as_view(), name='github_callback'),
]