"""
Django settings for demo project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'foc!ayo2il)#q@g^7y!v1t)ae7o6drdrwton%+gzbl!y=ihtdf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['example.com']

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Local apps
    'demo_oauth',

    # Trird party apps
    'socialaccess',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/var/www/static',
]


# django-socialaccess settings

FACEBOOK_KEY = '1023654184430110'
FACEBOOK_SECRET = '17a5dc215ab7e6bf0b6902dd21d27363'
#FACEBOOK_CONNECT_IMAGE = ''
FACEBOOK_CONNECT_CLASS = 'btn btn-facebook btn-block fa fa-facebook'
FACEBOOK_CONNECT_TEXT = ' Connect with Facebook'
FACEBOOK_SCOPE = 'public_profile,email'

GOOGLE_KEY = '885604431543-e42oekfhnmtm564trgnl1p01ni4244vu.apps.googleusercontent.com'
GOOGLE_SECRET = 'rmm-sQAulYSrsy73vXH1ftsB'
#GOOGLE_CONNECT_IMAGE = ''
GOOGLE_CONNECT_CLASS = 'btn btn-google btn-block fa fa-google-plus'
GOOGLE_CONNECT_TEXT = ' Connect with Google'
GOOGLE_SCOPE = 'https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile'

LINKEDIN_KEY = '75hzh89es2gf7y'
LINKEDIN_SECRET = 'WAovEwzd9Twq9kxY'
#LINKEDIN_CONNECT_IMAGE = ''
LINKEDIN_CONNECT_CLASS = 'btn btn-linkedin btn-block fa fa-linkedin'
LINKEDIN_CONNECT_TEXT = ' Connect with LinkedIn'
LINKEDIN_SCOPE = 'r_basicprofile r_emailaddress'

GITHUB_KEY = '47ae609a23644e316666'
GITHUB_SECRET = 'fb00835373875fbc6482aeb041e29d2b965ad95f'
#GITHUB_CONNECT_IMAGE = ''
GITHUB_CONNECT_CLASS = 'btn btn-github btn-block fa fa-github'
GITHUB_CONNECT_TEXT = ' Connect with GitHub'
GITHUB_SCOPE = 'r_basicprofile r_emailaddress'

SOCIALACCESS_MERGE_ACCOUNTS = True
SOCIALACCESS_AUTH_REDIRECT = '/authuser'

