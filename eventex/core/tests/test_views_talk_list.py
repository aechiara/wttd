# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from ..models import Speaker, Talk


class TalkListTest(TestCase):
    def setUp(self):
        s= Speaker.objects.create(name='Alex Chiaranda',
                slug='alex-chiaranda',
                url='http://www.outofmemory.blog.br',
                description='I am a passionate python developer !')
        t1 = Talk.objects.create(description=u'Tema da Palestra',
                title=u'Título da Palestra', start_time='10:00')
        t2 = Talk.objects.create(description=u'Tema da Palestra',
                title=u'Título da Palestra', start_time='13:00')
        t1.speakers.add(s)
        t2.speakers.add(s)

        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        ''' GET must result in 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        ''' Template should be core/talk_list.html '''
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        ''' Html should show talks '''
        self.assertContains(self.resp, u'Título da Palestra', 2)
        self.assertContains(self.resp, u'10:00')
        self.assertContains(self.resp, u'13:00')
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/alex-chiaranda', 2)
        self.assertContains(self.resp, u'I am a passionate python developer !', 2)
        self.assertContains(self.resp, u'Alex Chiaranda', 2)
        self.assertContains(self.resp, u'Tema da Palestra', 2)

    def test_morning_talks(self):
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talks(self):
        self.assertIn('afternoon_talks', self.resp.context)
