===================
Django Socialaccess
===================

This application is an OAuth based client for Django sites. It is powered by the python oauth2 client implementation and supports both the oauth and the oauth2 versions.
Django socialaccess permits user authentication and api access to a limited list of oauth providers and their APIs.


Requirements
============
Django >= 1.8

oauth2 1.5.211

Installation
============
1. Get and install

    pip install git+https://github.com/fireinthehole/django-socialaccess.git

    or clone it:

    git clone git://github.com/fireinthehole/django-socialaccess.git

2. Add the application to your Django INSTALLED_APPS in settings.py

    INSTALLED_APPS = (
    ...
    'socialaccess',
    ...
    )

3. Add your keys/secrets from the sites to connect from in your settings.py

    LINKEDIN_KEY           = 'app key'

    LINKEDIN_SECRET        = 'secret'

    LINKEDIN_CONNECT_IMAGE = 'an url to a connect icon'


    FACEBOOK_KEY           = ...

    FACEBOOK_SECRET        = ..

    FACEBOOK_CONNECT_IMAGE = .


    TWITTER_KEY           = 

    TWITTER_SECRET        = 

    TWITTER_CONNECT_IMAGE = 


    GOOGLE_KEY           = 

    GOOGLE_SECRET        = 

    GOOGLE_EMAIL_ADDR    = 

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
