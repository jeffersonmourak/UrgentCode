# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_users_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forums',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name=b'Nome')),
                ('descriptions', models.CharField(max_length=512, verbose_name=b'Descri\xc3\xa7\xc3\xa3o')),
                ('creator', models.ForeignKey(verbose_name=b'Criador', to='webapp.Users')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
