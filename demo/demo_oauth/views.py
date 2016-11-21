from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.sites.models import Site
from django.contrib.auth import logout
from demo_oauth.forms import LoginForm


User = get_user_model()

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


class AuthUser(View):
    """
        Login user before merging accounts
    """
    form_class = LoginForm 
    template_name = 'authuser.tpl'

    def get(self, request, *args, **kwargs):
        dest = request.GET['next']
        email = request.GET['email']
        success = kwargs.get('success')
        if request.user.is_authenticated():
            return redirect(dest)
        else:
            form = self.form_class(initial={'login': email, 'next': dest})
            return render(request, self.template_name, {'form': form, 'success':success })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # get this user by email
            try:
                user = User.objects.get(email=cd['login'])
            except User.DoesNotExist:
                form.add_error('login', 'User does not exist.')
                return render(request, self.template_name, {'form': form})
            
            if not user.is_active:
                form.add_error('login', 'This user account is not activated.')
                return render(request, self.template_name, {'form': form})

            user = authenticate(username=cd['login'], password=cd['password'])

            if user is not None:
                login(request, user)
                return redirect(cd['next'])

            form.add_error('password', 'Wrong password.')
        return render(request, self.template_name, {'form': form})
