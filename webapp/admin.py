#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models


admin.site.register(models.Users)
admin.site.register(models.Forums)
admin.site.register(models.Subscribers)
admin.site.register(models.Answers)
admin.site.register(models.Likes)