from django.conf import settings


AUTHENTICATION_BACKENDS    = getattr(settings, 'AUTHENTICATION_BACKENDS', ['django.contrib.auth.backends.ModelBackend',])
AUTHENTICATION_BACKENDS    += [
                                'socialaccess.auth.backends.OAuthFacebookBackend',
                                'socialaccess.auth.backends.OAuthLinkedinBackend',
                                'socialaccess.auth.backends.OAuthGoogleBackend',
                                'socialaccess.auth.backends.OAuthGithubBackend',
                             ]

FACEBOOK_REQUEST_CODE_URL  = 'https://www.facebook.com/v2.9/dialog/oauth'
FACEBOOK_ACCESS_TOKEN_URL  = 'https://graph.facebook.com/v2.9/oauth/access_token'
FACEBOOK_PROFILE_URL       = 'https://graph.facebook.com/v2.9/me'
FACEBOOK_SCOPE             = 'public_profile,email'

GOOGLE_REQUEST_CODE_URL    = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_ACCESS_TOKEN_URL    = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_PROFILE_URL         = 'https://www.googleapis.com/oauth2/v1/userinfo'
GOOGLE_SCOPE               = 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile'

LINKEDIN_REQUEST_CODE_URL  = 'https://www.linkedin.com/oauth/v2/authorization'
LINKEDIN_ACCESS_TOKEN_URL  = 'https://www.linkedin.com/oauth/v2/accessToken'
LINKEDIN_PROFILE_URL       = 'https://api.linkedin.com/v1/people/~:(id,email-address,firstName,lastName)'
LINKEDIN_SCOPE             = 'r_basicprofile r_emailaddress'

GITHUB_REQUEST_CODE_URL    = 'https://github.com/login/oauth/authorize'
GITHUB_ACCESS_TOKEN_URL    = 'https://github.com/login/oauth/access_token'
GITHUB_PROFILE_URL         = 'https://api.github.com/users/me'
GITHUB_SCOPE               = 'user:email'