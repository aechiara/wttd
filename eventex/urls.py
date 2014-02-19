from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventex.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # subscriptions
    url(r'^inscricao/', include('eventex.subscriptions.urls', namespace='subscriptions')),

    # core
    url(r'', include('eventex.core.urls', namespace='core')),
)
