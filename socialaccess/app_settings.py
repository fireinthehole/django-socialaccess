from django.conf import settings


AUTHENTICATION_BACKENDS    = getattr(settings, 'AUTHENTICATION_BACKENDS', ('django.contrib.auth.backends.ModelBackend',))
AUTHENTICATION_BACKENDS    += (
                                'socialaccess.auth.backends.OAuthFacebookBackend',
                                'socialaccess.auth.backends.OAuthLinkedinBackend',
                                'socialaccess.auth.backends.OAuthTwitterBackend',
                                'socialaccess.auth.backends.OAuthGoogleBackend',
                                'socialaccess.auth.backends.OAuthGithubBackend',
                             )

LINKEDIN_REQUEST_TOKEN_URL = 'https://api.linkedin.com/uas/oauth/requestToken'
LINKEDIN_AUTHORIZE_URL     = 'https://api.linkedin.com/uas/oauth/authorize'
LINKEDIN_ACCESS_TOKEN_URL  = 'https://api.linkedin.com/uas/oauth/accessToken'
LINKEDIN_PROFILE_URL       = 'http://api.linkedin.com/v1/people/'

FACEBOOK_REQUEST_CODE_URL  = 'https://www.facebook.com/dialog/oauth'
FACEBOOK_ACCESS_TOKEN_URL  = 'https://graph.facebook.com/oauth/access_token'
FACEBOOK_PROFILE_URL       = 'https://graph.facebook.com'

TWITTER_REQUEST_TOKEN_URL  = 'https://api.twitter.com/oauth/request_token'
TWITTER_AUTHORIZE_URL      = 'https://api.twitter.com/oauth/authenticate'
TWITTER_ACCESS_TOKEN_URL   = 'https://api.twitter.com/oauth/access_token'
TWITTER_PROFILE_URL        = ''

GOOGLE_REQUEST_CODE_URL    = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_ACCESS_TOKEN_URL    = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_PROFILE_URL         = 'https://www.googleapis.com/oauth2/v1/userinfo'

GITHUB_REQUEST_CODE_URL    = 'https://github.com/login/oauth/authorize'
GITHUB_ACCESS_TOKEN_URL    = 'https://github.com/login/oauth/access_token'
GITHUB_PROFILE_URL         = 'https://github.com/api/v2/json/user/show'