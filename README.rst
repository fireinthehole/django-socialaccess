===================
Django Socialaccess
===================

Simple django authentication client for a list of providers implementing the OAuth 2 protocol.
Actually the supported providers are Facebook, Google and Linkedin.


Requirements
============
Python 3

Django >= 1.9


Installation
============
``git clone git://github.com/fireinthehole/django-socialaccess.git``

Installing the django-socialaccess package is performed as usual

``python3 setup.py install``

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

- Create the OAuth providers connect buttons

 django-socialaccess connect buttons are custom tags. Load the template tags library inside the login page template of your web site and place the connect buttons.

 ``{% load connect_buttons %}``

 ...

 ``{% connect_button google %}``

 ``{% connect_button facebook %}``

 ``{% connect_button linkedin %}``

 ...

- Create the django-socialaccess extended profiles

 ``python manage.py makemigrations socialaccess``

 ``python manage.py migrate``

- Set your site domain name

 From the django admin interface, set ``site.domain`` to your web site domain name

 In the demo example, the used domain is example.com:8000.
 For localhost set up example.com in /etc/hosts
