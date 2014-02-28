# coding: utf-8
from django.test import TestCase
from ..models import Talk, Course
from ..managers import PeriodManager


class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
                title=u'Introdução ao Django',
                description=u'Descrição da palestra.',
                start_time='10:00')

    def test_create(self):
        self.assertEqual(1, len(Talk.objects.all()))

    def test_unicode(self):
        self.assertEqual(self.talk.title, unicode(self.talk))

    def test_speakers(self):
        ''' Talk has many speakers and vice-versa '''
        self.talk.speakers.create(name='Alex Chiaranda',
                slug='alex-chiaranda',
                url='http://www.outofmemory.blog.br')
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        ''' Talk default manager must be instance of PeriodManager '''
        self.assertIsInstance(Talk.objects, PeriodManager)


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title=u'Mini Curso Django',
                description=u'Descrição do Minicurso', start_time='10:00', slots=20)

    def test_create(self):
        self.assertEqual(1, Course.objects.all().count())

    def test_unicode(self):
        self.assertEqual(self.course.title, unicode(self.course))

    def test_speakers(self):
        ''' Course can have many speakers and vice-versa '''
        self.course.speakers.create(name='Alex Chiaranda', slug='alex-chiaranda',
                url='http://www.outofmemory.blog.br')
        self.assertEqual(1, self.course.speakers.count())

    def test_period_manager(self):
        ''' Course default Manager must be PeriodManager '''
        self.assertIsInstance(Course.objects, PeriodManager)
