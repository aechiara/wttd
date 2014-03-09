# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import SubscriptionDetail, SubscriptionCreate

urlpatterns = patterns('eventex.subscriptions.views',
    #url(r'^$', 'subscribe', name='subscribe'),
    url(r'^$', SubscriptionCreate.as_view(), name='subscribe'),
    #url(r'^(\d+)/$', 'detail', name='detail'),
    url(r'^(?P<pk>\d+)/$', SubscriptionDetail.as_view(), name='detail'),
    url(r'^api/get_emails/', 'get_emails', name='get_emails'),
    url(r'^api/validate_cpf/', 'validate_cpf', name='validate_cpf'),
)
