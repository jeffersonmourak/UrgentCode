#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from webapp import views, forums, actions

urlpatterns = patterns('',
    url(r'^$',views.index, name="Index Page"),

    url(r'^forum/$',forums.index, name="Index Page"),
    url(r'^forum/dashboard/$',forums.dashboard, name="Index Page"),
    url(r'^forum/login/$',forums.loginView, name="Index Page"),
    url(r'^forum/logout/$',forums.logout, name="Index Page"),
    url(r'^forum/(?P<user>\S+)/(?P<forum>\S+)$',forums.view, name="Index Page"),

    url(r'^actions/like/(?P<user>\S+)/(?P<forum>\S+)/(?P<answer>\S+)$',actions.like, name="Index Page"),
    url(r'^actions/unlike/(?P<user>\S+)/(?P<forum>\S+)/(?P<answer>\S+)$',actions.unlike, name="Index Page"),
    url(r'^actions/reply/(?P<user>\S+)/(?P<forum>\S+)$',actions.reply, name="Index Page"),


    url(r'^admin/', include(admin.site.urls)),
)
