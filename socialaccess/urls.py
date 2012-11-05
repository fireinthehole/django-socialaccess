from django.conf.urls import patterns, include, url

from socialaccess.views import LinkedinConnect, LinkedinCallback, \
                               FacebookConnect, FacebookCallback, \
                               TwitterConnect, TwitterCallback, \
                               GoogleConnect, GoogleCallback, \
                               GithubConnect, GithubCallback


urlpatterns = patterns('socialaccess.views',
    url(r'^fblogin/$', FacebookConnect.as_view(), name='fb_connect'),
    url(r'^fbcallback/$', FacebookCallback.as_view(), name='fb_callback'),

    url(r'^linkedinlogin/$', LinkedinConnect.as_view(), name='linkedin_connect'),
    url(r'^linkedincallback/$', LinkedinCallback.as_view(), name='linkedin_callback'),

    url(r'^twitterlogin/$', TwitterConnect.as_view(), name='twitter_connect'),
    url(r'^twittercallback/$', TwitterCallback.as_view(), name='twitter_callback'),

    url(r'^googlelogin/$', GoogleConnect.as_view(), name='google_connect'),
    url(r'^googlecallback/$', GoogleCallback.as_view(), name='google_callback'),

    url(r'^githublogin/$', GithubConnect.as_view(), name='github_connect'),
    url(r'^githubcallback/$', GithubCallback.as_view(), name='github_callback'),
)