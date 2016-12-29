"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from socialaccess.urls import urlpatterns as oauth_urls
from demo_oauth.views import Home, Logout, AuthUser


# handler400 = 'demo.views.my_handler400'
# handler403 = 'demo.views.my_handler403'
# handler404 = 'demo.views.my_handler404'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^authuser/', AuthUser.as_view(), name='authuser'),
    url(r'^$', Home.as_view(), name='home'),

    # django-socialaccess urls
    url(r'^socialaccess/', include(oauth_urls), name='socialaccess'),
]

