# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url

from web.views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name="web.index"),
)
