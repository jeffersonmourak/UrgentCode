# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='likes',
            options={'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
    ]
