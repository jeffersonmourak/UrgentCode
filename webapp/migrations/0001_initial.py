# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(unique=True, serialize=False, verbose_name=b'Id', primary_key=True)),
                ('name', models.CharField(max_length=45, verbose_name=b'Nome')),
                ('surname', models.CharField(max_length=45, verbose_name=b'Sobrenome')),
                ('email', models.CharField(max_length=256, verbose_name=b'email')),
                ('password', models.CharField(max_length=256, verbose_name=b'Senha')),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
            bases=(models.Model,),
        ),
    ]
