===================
Django Socialaccess
===================

Simple django authentication client for a list of providers implementing the OAuth 2 protocol.
Actually the supported providers are Facebook, Google, Linkedin and Github.


Requirements
============
Python 3

Django >= 1.9


Installation
============
``git clone git://github.com/fireinthehole/django-socialaccess.git``

``cd django-socialaccess``

``pip install .``


Configuration
=============
- Add ``socialaccess`` to INSTALLED_APPS in your django settings.py

 ``INSTALLED_APPS = [``

 ``..``

 ``'socialaccess',``

 ``..``
 ``]``

- Activate the Django Sites framework in settings.py

 Add ``SITE_ID``

 Add ``django.contrib.sites`` to ``INSTALLED_APPS``

- Set the default http protocol in production

 ``DEFAULT_HTTP_PROTOCOL = 'https'``

- Add the app credentials for each provider you want to use as follows:

 For facebook:

 ``FACEBOOK_KEY = 'your app key'``

 ``FACEBOOK_SECRET = 'your app secret'``

 ``FACEBOOK_SCOPE = 'public_profile,email'`` (at least ``'public_profile,email'`` depending that data you want to retrieve from the provider)

- Configure the connect buttons style

 ``FACEBOOK_CONNECT_CLASS = 'custom css classes'``
 
 or
 
 ``FACEBOOK_CONNECT_IMAGE = 'url to the connect button image'``

- For each provider the settings variable are prefixed by its name the same way

 For linkedin:

 ``LINKEDIN_KEY, LINKEDIN_SECRET, LINKEDIN_SCOPE, LINKEDIN_CONNECT_CLASS, LINKEDIN_CONNECT_IMAGE..``

 For google:

 ``GOOGLE_KEY, GOOGLE_SECRET, GOOGLE_SCOPE, GOOGLE_CONNECT_CLASS, GOOGLE_CONNECT_IMAGE..``

 For github:

 ``GITHUB_KEY, GITHUB_SECRET, GITHUB_SCOPE, GITHUB_CONNECT_CLASS, GITHUB_CONNECT_IMAGE..``

- Create the OAuth providers connect buttons

 django-socialaccess connect buttons are custom tags. Load the template tags library inside the login page template of your web site and place the connect buttons.

 ``{% load connect_buttons %}``

 ...

 ``{% connect_button google %}``

 ``{% connect_button facebook %}``

 ``{% connect_button linkedin %}``

 ``{% connect_button github %}``

 ...

- Create the django-socialaccess extended profiles

 ``python manage.py migrate``

- Set your site domain name

 From the django admin interface, set ``site.domain`` to your web site domain name

 In the demo example, the used domain is example.com:8000.
 For localhost set up example.com in /etc/hosts

- Callback urls

  While creating your apps on the provider side, you may be asked to give your site callback urls.
  They actually are:

  ``/socialaccess/fbcallback``

  ``/socialaccess/linkedincallback``

  ``/socialaccess/googlecallback``

  ``/socialaccess/githubcallback``


Merging multiple OAuth accounts
===============================

If you need this option, you should set two additional variables to your project ``settings.py`` and implement a password login form page. 

  ``SOCIALACCESS_MERGE_ACCOUNTS = True``

  ``SOCIALACCESS_AUTH_REDIRECT = /your_user_auth_url``

Users can authenticate using multiple OAuth providers. This kind of authentication is possible if a user have the same email for each OAuth provider account. 

In this case a new extended profile is being created per provider and associated with the primary user account.

An additional intermediate authentication by password should take place in the OAuth flow to ensure the user identity. While authenticating by a new OAuth provider for the very first time, the user is redirected to an ordinal login form just after acquiring the OAuth token. This is the social account association step and occurs only once. Each ulterior authentication is carried out directly.

For this purpose your should implement an ordinal login page.
On successful login the user should be redirected to the request.GET['next'] value so that the ``django-socialaccess`` OAuth flow may terminate correctly.
