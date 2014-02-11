from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # core
    url(r'^$', 'eventex.core.views.home', name = 'home'),

    # subscriptions
    url(r'^inscricao/$', 'eventex.subscriptions.views.subscribe', name='subscribe'),
    url(r'^inscricao/(\d+)/$', 'eventex.subscriptions.views.detail', name='detail'),


    url(r'^admin/', include(admin.site.urls)),
)
