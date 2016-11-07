from django.conf import settings


AUTHENTICATION_BACKENDS    = getattr(settings, 'AUTHENTICATION_BACKENDS', ['django.contrib.auth.backends.ModelBackend',])
AUTHENTICATION_BACKENDS    += [
                                'socialaccess.auth.backends.OAuthFacebookBackend',
                                'socialaccess.auth.backends.OAuthLinkedinBackend',
                                'socialaccess.auth.backends.OAuthGoogleBackend',
                             ]

FACEBOOK_REQUEST_CODE_URL  = 'https://www.facebook.com/dialog/oauth'
FACEBOOK_ACCESS_TOKEN_URL  = 'https://graph.facebook.com/oauth/access_token'
FACEBOOK_PROFILE_URL       = 'https://graph.facebook.com/me'

GOOGLE_REQUEST_CODE_URL    = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_ACCESS_TOKEN_URL    = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_PROFILE_URL         = 'https://www.googleapis.com/oauth2/v1/userinfo'

LINKEDIN_REQUEST_CODE_URL  = 'https://www.linkedin.com/oauth/v2/authorization'
LINKEDIN_ACCESS_TOKEN_URL  = 'https://www.linkedin.com/oauth/v2/accessToken'
LINKEDIN_PROFILE_URL       = 'https://api.linkedin.com/v1/people/~:(id,email-address,firstName,lastName)'
