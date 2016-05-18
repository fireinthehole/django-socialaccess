===================
Django Socialaccess
===================

This application is an OAuth client for django web apps. It is powered by the python-oauth2 client library and supports both the oauth 1.0 and the oauth2 versions.
Django socialaccess is designed for cross-site authentication, but it also provides an http client for server-side quering on the application available providers APIs.


Requirements
============
Django >= 1.9

oauth2 == 1.9rc1

Installation
============
1. Get and install

    pip install git+https://github.com/fireinthehole/django-socialaccess.git

2. Add socialaccess to your Django INSTALLED_APPS in settings.py

    INSTALLED_APPS = [
    ...
    'socialaccess',
    ...
    ]

3. Add your keys/secrets from the sites to connect from in your settings.py

    LINKEDIN_KEY           = 'app key'

    LINKEDIN_SECRET        = 'secret'

    LINKEDIN_CONNECT_IMAGE = 'url to a connect icon'
    or 
    LINKEDIN_CONNECT_CLASS = 'fa fa-linkedin' for fontawesome img or a custom css class


    FACEBOOK_KEY           = ...

    FACEBOOK_SECRET        = ..

    FACEBOOK_CONNECT_IMAGE = .


    TWITTER_KEY           = 

    TWITTER_SECRET        = 

    TWITTER_CONNECT_IMAGE = 


    GOOGLE_KEY           = 

    GOOGLE_SECRET        = 

    GOOGLE_CONNECT_IMAGE = 


    GITHUB_KEY           = 

    GITHUB_SECRET        = 

    GITHUB_CONNECT_IMAGE = 

No other settings are required. 
The rest of the settings, such as custom authentication backends and OAuth servers request/access token urls are loaded implicitely into the settings.py

4. Create the extended profiles
    python manage.py syncdb

5. The authentication is working by simply adding a tag from the following list inside your login page template. 

    {% connect_button google %}

    {% connect_button facebook %}

    {% connect_button linkedin %}

    {% connect_button twitter %}

    {% connect_button github %}
