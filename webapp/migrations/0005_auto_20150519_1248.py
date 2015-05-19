# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_forums'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forums',
            options={'verbose_name': 'Forum', 'verbose_name_plural': 'Foruns'},
        ),
    ]
