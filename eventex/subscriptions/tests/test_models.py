# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from eventex.subscriptions.models import Subscription
from datetime import datetime

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
                name='Alex Eduardo Chiaranda',
                cpf='12345678901',
                email='aechiara@gmail.com',
                phone='11-912345678'
                )

    def test_create(self):
        ''' Subscription must have name cpf, email, phone '''
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        ''' Subscription must have automatic created_at '''
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        ''' Unicode should return name '''
        self.assertEqual(unicode(self.obj.name), unicode(self.obj))

    def test_paid_default_value_is_False(self):
        ''' By default paid must be False '''
        self.assertEqual(False, self.obj.paid)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
                name='Alex Eduardo Chiaranda', cpf='12345678901',
                email='aechiara@gmail.com', phone='11-912345678'
                )

    def test_cpf_unique(self):
        ''' CPF must be unique '''
        s = Subscription(
                name='Alex Eduardo Chiaranda', cpf='12345678901',
                email='aechiara@gmail.com', phone='11-912345678'
                )
        self.assertRaises(IntegrityError, s.save)

    #def test_email_unique(self):
        #''' Email must be unique '''
        #s = Subscription(
                #name='Alex Eduardo Chiaranda', cpf='12345678900',
                #email='aechiara@gmail.com', phone='11-912345678'
                #)
        #self.assertRaises(IntegrityError, s.save)

    def test_email_not_unique(self):
        s = Subscription.objects.create(
                name='Alex Eduardo Chiaranda', cpf='12345678902',
                email='aechiara@gmail.com', phone='11-912345678'
                )
        self.assertEqual(2, len(Subscription.objects.all()))

