# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from ..models import Speaker


class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(name='Alex Chiaranda',
                slug = 'alex-chiaranda',
                url = 'http://www.outofmemory.blog.br',
                description = 'Passionate python developer')

        url = r('core:speaker_detail', kwargs={'slug': 'alex-chiaranda'})
        self.resp = self.client.get(url)

    def test_get(self):
        ''' Get should result in 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        ''' Template should be core/speaker_detail.html '''
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        self.assertContains(self.resp, 'Alex Chiaranda')
        self.assertContains(self.resp, 'Passionate python developer')
        self.assertContains(self.resp, 'http://www.outofmemory.blog.br')

    def test_context(self):
        ''' Speaker must be in a context '''
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)
