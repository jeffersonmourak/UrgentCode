# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_users_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='', max_length=45, verbose_name=b'Nome de usu\xc3\xa1rio'),
            preserve_default=False,
        ),
    ]
