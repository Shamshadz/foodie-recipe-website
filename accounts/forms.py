from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


# class userForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#         labels = {
#             'username': _('UserName'),
#             'email' : _('Email'),
#             'password1' : _('Password'),
#             'password2'  : _('Confirm Password'),
#         }