# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _


class SubscriptionForm(forms.Form):
    name = forms.CharField(label=_('Nome'))
    cpf = forms.CharField(label=_('CPF'), max_length=11)
    email = forms.EmailField(label=_('E-Mail'))
    phone = forms.CharField(label=_('Telefone'))
