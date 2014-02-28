# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from ..models import Talk


class TalkDetailTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='10:00')
        t.speakers.create(name='Alex Chiaranda', slug='alex-chiaranda')
        self.resp = self.client.get(r('core:talk_detail', args=[1]))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')

    def test_talk_in_context(self):
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_not_found(self):
        response = self.client.get(r('core:talk_detail', args=[0]))
        self.assertEquals(404, response.status_code)

    def test_html(self):
        self.assertContains(self.resp, 'Talk')
        self.assertContains(self.resp, '/palestrantes/alex-chiaranda')
        self.assertContains(self.resp, 'Alex Chiaranda')
