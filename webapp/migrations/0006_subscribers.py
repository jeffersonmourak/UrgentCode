# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20150519_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribers',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('forum', models.ForeignKey(verbose_name=b'Forum', to='webapp.Forums')),
                ('subscribers', models.ManyToManyField(to='webapp.Users', verbose_name=b'Inscritos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
