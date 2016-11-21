from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form): 

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].error_messages = {'required': 'Password is required.'}

    login = forms.CharField(widget=forms.TextInput(
                                attrs={'class':"form-control", 'required':True, 'readonly': True}))
    password = forms.CharField(min_length=4, 
                                max_length=16, 
                                widget=forms.PasswordInput(
                                    attrs={'placeholder': 'Enter your password', 'class':"form-control", 'required':True, 'autofocus':True}))
    next = forms.CharField(widget=forms.HiddenInput(
                                attrs={'class':"form-control", 'required':True}))

    def is_valid(self):
        valid = super(LoginForm, self).is_valid()
        return valid