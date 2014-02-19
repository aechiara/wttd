# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        ''' Form must have 4 fields '''
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        ''' CPF must accept only digits '''
        form = self.make_validated_form(cpf='ABC123')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        ''' Raise error is CPF does not have 11 digits '''
        form = self.make_validated_form(cpf='1234')
        self.assertItemsEqual(['cpf'], form.errors)

    def test_email_is_optional(self):
        ''' Email is optional '''
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Alex Eduardo Chiaranda', email='aechiara@gmail.com', cpf='12345678901', phone='11-1234-5678')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
