# coding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('eventex.subscriptions.views',
    url(r'^$', 'subscribe', name='subscribe'),
    url(r'^(\d+)/$', 'detail', name='detail'),
    url(r'^api/get_emails/', 'get_emails', name='get_emails'),
    url(r'^api/validate_cpf/', 'validate_cpf', name='validate_cpf'),
)
