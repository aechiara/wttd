# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        self.s = Subscription.objects.create(name='Alex Eduardo Chiaranda', cpf='12345678901', email='aechiara@gmail.com', phone='11-912345678')
        self.resp = self.client.get('/inscricao/%d/' % self.s.pk)

    def test_get(self):
        ''' GET /inscricao/1 should return 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        ''' Must use template '''
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        ''' Must have a Subscription instance '''
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        ''' Check if subscription was renderead '''
        self.assertContains(self.resp, self.s.name)


class DetailNotFound(TestCase):
    def test_not_found(self):
        ''' Must return 404 when not found '''
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)
