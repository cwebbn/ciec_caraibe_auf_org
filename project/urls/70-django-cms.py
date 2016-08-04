# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns += i18n_patterns('',
    url(r'^', include('cms.urls')),
)
