from django.conf.urls import url

from socialaccess.views import (
    FacebookConnectView, FacebookCallbackView, FacebookMergeView,
    LinkedinConnectView, LinkedinCallbackView, LinkedinMergeView,
    GoogleConnectView, GoogleCallbackView, GoogleMergeView,
    GithubConnectView, GithubCallbackView, GithubMergeView,
)


urlpatterns = [
    url(r'^fblogin/$', FacebookConnectView.as_view(), name='fb_connect'),
    url(r'^fbcallback/$', FacebookCallbackView.as_view(), name='fb_callback'),
    url(r'^fbmerge/$', FacebookMergeView.as_view(), name='fb_merge'),

    url(r'^linkedinlogin/$', LinkedinConnectView.as_view(), name='linkedin_connect'),
    url(r'^linkedincallback/$', LinkedinCallbackView.as_view(), name='linkedin_callback'),
    url(r'^linkedinmerge/$', LinkedinMergeView.as_view(), name='linkedin_merge'),

    url(r'^googlelogin/$', GoogleConnectView.as_view(), name='google_connect'),
    url(r'^googlecallback/$', GoogleCallbackView.as_view(), name='google_callback'),
    url(r'^googlemerge/$', GoogleMergeView.as_view(), name='google_merge'),

    url(r'^githublogin/$', GithubConnectView.as_view(), name='github_connect'),
    url(r'^githubcallback/$', GithubCallbackView.as_view(), name='github_callback'),
    url(r'^githubmerge/$', GithubMergeView.as_view(), name='github_merge'),
]