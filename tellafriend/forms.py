# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

try:
    from captcha.fields import CaptchaField
except ImportError:
    raise ImportError, "django-tellafriend requires django-simple-captcha"


class TellAFriendForm(forms.Form):
    url = forms.CharField(max_length=200, label=_("URL"), widget=forms.HiddenInput)
    email_sender = forms.EmailField(max_length=100, label=_("Sender"))
    email_recipient = forms.EmailField(max_length=100, label=_("Recipient"))
    message = forms.CharField(required=False, widget=forms.Textarea, label=_("Message"))
    captcha = CaptchaField(help_text=_("Please enter the characters shown in the image in the field next to it."), label=_("Captcha"))