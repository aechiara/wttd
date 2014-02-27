# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.urlresolvers import reverse as r
from ..models import Speaker, Contact


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Alex Chiaranda',
                slug='alex-chiaranda',
                url='http://www.outofmemory.blog.br',
                description='Passionate python developer')
        self.speaker.save()

    def test_create(self):
        ''' Speaker instance should be saved '''
        self.assertEqual(1, len(Speaker.objects.all()))

    def test_slug_must_be_unique(self):
        ''' Slug field must be unique '''
        speaker = Speaker(name='Alex Chiaranda 2',
                slug='alex-chiaranda',
                url='http://www.outofmemory.blog.br',
                description='Passionate python developer')
        self.assertRaises(IntegrityError, speaker.save)

    def test_unicode(self):
        ''' Speaker string representation should be the name '''
        self.assertEqual(u'Alex Chiaranda', unicode(self.speaker))


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        url = r('core:speaker_detail', kwargs={'slug': 'john-doe'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)



class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Alex Chiaranda',
                slug='alex-chiaranda',
                url='http://www.outofmemory.blog.br',
                description='Passionate python developer')

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E',
                value='aechiara@gmail.com')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P',
                value='11-912345678')
        self.assertEqual(1, contact.pk)

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='F',
                value='11-12345678')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        ''' Contact kind must be limited to E, P or F '''
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        ''' Contact string representation should be value '''
        contact = Contact.objects.create(speaker=self.speaker, kind='E',
                value='aechiara@gmail.com')
        self.assertEqual(contact.value, unicode(contact))
