from django.conf import settings
from django.views.generic.base import View
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, get_user_model
from socialaccess.mixins import (
    FacebookViewMixin, GoogleViewMixin, LinkedinViewMixin, GithubViewMixin
)


User = get_user_model()

MERGE_ACCOUNTS = getattr(settings, 'SOCIALACCESS_MERGE_ACCOUNTS', False)


class AbstractOAuth2ConnectView(View):
    """
    """
    def get(self, request):
        oauth2_client = self.get_oauth2_client()
        authorize_url = oauth2_client.get_authorize_url()
        request.session['state'] = oauth2_client.state
        return redirect(authorize_url)


class AbstractOAuth2CallbackView(View):
    """
    """
    def get(self, request):
        oauth_verifier = request.GET.get('code')

        # CSRF check
        if request.session['state'] != request.GET['state']:
            return HttpResponse('The state param does not match!', status=401)
        del request.session['state']

        # Check if any error occured at the redirect step
        error_message = request.GET.get('error_message') or request.GET.get('error_description')
        if error_message:
            return HttpResponse('An error occured on the callback step: {}'.format(error_message), status=400)

        oauth2_client = self.get_oauth2_client()

        # Get the access token
        try:
            access_token = oauth2_client.get_access_token(oauth_verifier=oauth_verifier)
        except Exception as e:
            return HttpResponse(e, status=401)

        # Request the oauth provider API to get the user's profile info
        try:
            user_data = oauth2_client.get_profile_info(access_token)
        except Exception as e:
            return HttpResponse(e, status=401)

        # Try to authenticate a user already registered with oauth
        user = oauth2_client.authenticate(user_data['id'])

        if user is None:
            # User does not exist
            try:
                #TODO: hook for unavailable user profile fields

                # Look for a user alreday registered without oauth
                user = User.objects.get(email=user_data.get('email'))
                
                if MERGE_ACCOUNTS:
                    # Create a new social account.
                    if user.has_usable_password():
                        # Store the access token in the session
                        # Redirect the user to an ordinal authentication page
                        # On success the user should be redirected to the account merge url 
                        # where the new social account association is taking place using the previously session stored access_token
                        request.session['access_token'] = access_token
                        auth_uri = getattr(settings, 'SOCIALACCESS_AUTH_REDIRECT')
                        return redirect('{}?email={}&next={}'.format(auth_uri, user.email, self.merge_uri))
                    else:
                        # In this case we have one or more social accounts associated to an account who still has not set a password
                        # Here no ordinal authentication could take place
                        oauth2_client.create_profile(user_data, access_token)
                        user = oauth2_client.authenticate(user_data['id'])
                else:
                    # Refuse to authenticate if an account using the same email already exists
                    return HttpResponse('User {id} already exists without social account association. Please authenticate using the login form.'.format(
                        id=user_data.get('email')),
                        status=400
                    )
            except User.DoesNotExist:
                # Create a new account with social account association
                oauth2_client.create_profile(user_data, access_token)
                user = oauth2_client.authenticate(user_data['id'])

        # Update the user access_token
        oauth2_client.update_access_token(user.email, access_token)

        login(request, user)
        return redirect('/')


class AbstractMergeAccountView(View):
    """
    """
    def get(self, request):
        """
        """
        if not MERGE_ACCOUNTS:
            return HttpResponse('Profile merge is not allowed', status=401)

        if request.user.is_authenticated():
            access_token = request.session['access_token']
            oauth2_client = self.get_oauth2_client()
            del request.session['access_token']

            # Request the oauth provider API to get the user's profile info
            try:
                user_data = oauth2_client.get_profile_info(access_token)
                oauth2_client.create_profile(user_data, access_token)
                return redirect('/')
            except Exception as e:
                return HttpResponse(e, status=401)
        return HttpResponse(status=403)


# Facebook views
class FacebookConnectView(AbstractOAuth2ConnectView, FacebookViewMixin):
    pass


class FacebookCallbackView(AbstractOAuth2CallbackView, FacebookViewMixin):
    pass


class FacebookMergeView(AbstractMergeAccountView, FacebookViewMixin):
    pass


# Google views
class GoogleConnectView(AbstractOAuth2ConnectView, GoogleViewMixin):
    pass


class GoogleCallbackView(AbstractOAuth2CallbackView, GoogleViewMixin):
    pass


class GoogleMergeView(AbstractMergeAccountView, GoogleViewMixin):
    pass


# Linkedin views
class LinkedinConnectView(AbstractOAuth2ConnectView, LinkedinViewMixin):
    pass


class LinkedinCallbackView(AbstractOAuth2CallbackView, LinkedinViewMixin):
    pass


class LinkedinMergeView(AbstractMergeAccountView, LinkedinViewMixin):
    pass


# Github views
class GithubConnectView(AbstractOAuth2ConnectView, GithubViewMixin):
    pass


class GithubCallbackView(AbstractOAuth2CallbackView, GithubViewMixin):
    pass


class GithubMergeView(AbstractMergeAccountView, GithubViewMixin):
    pass
