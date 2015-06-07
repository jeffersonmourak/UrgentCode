#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models

class ForumsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('name',)}

admin.site.register(models.Users)
admin.site.register(models.Forums,ForumsAdmin)
admin.site.register(models.Followers)
admin.site.register(models.Answers)
admin.site.register(models.Likes)