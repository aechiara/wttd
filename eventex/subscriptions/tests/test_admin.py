# coding: utf-8
from django.test import TestCase
from mock import Mock
from ..admin import SubscriptionAdmin, Subscription, admin


class MarkAsPaidTest(TestCase):
    def setUp(self):
        # Instancia o Model Admin
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)

        # popula o banco
        Subscription.objects.create(name='Alex Eduardo Chiaranda', cpf='12345678901', email='aechiara@gmail.com')

    def test_has_action_mark_as_paid(self):
        ''' Action mark_as_paid installed '''
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
