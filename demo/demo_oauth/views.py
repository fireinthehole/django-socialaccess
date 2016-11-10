from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.sites.models import Site
from django.contrib.auth import logout

# Create your views here.

class Home(View):
    template_name = 'home.tpl'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'user': request.user,
            'site': Site.objects.get_current(),
        })


class Logout(View):
    template_name = 'logout.tpl'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse('home'))