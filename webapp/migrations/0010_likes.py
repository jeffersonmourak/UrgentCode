# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20150519_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('answer', models.ForeignKey(verbose_name=b'Resposta', to='webapp.Answers')),
                ('user', models.ForeignKey(verbose_name=b'Usu\xc3\xa1rio', to='webapp.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
