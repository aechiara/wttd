# coding: utf-8
from django.test import TestCase
from ..models import Talk, Media


class MediaModelTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title='Talk', start_time='10:00')
        self.media = Media.objects.create(talk=t, kind='YT', media_id='fSnBF-BmccQ', title='Video')

    def test_create(self):
        self.assertEqual(1, Media.objects.all().count())

    def test_unicode(self):
        self.assertEqual('%s - %s' % (self.media.talk, self.media.title), unicode(self.media))
